from django.contrib import admin
from django.core import urlresolvers
from django import forms
from flatblocks.models import FlatBlock
 
class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['slug',]
    list_display = ('slug', 'header', 'content')
    search_fields = ('slug', 'header', 'content')
    
    def get_form(self, request, obj=None, **kwargs):
        Form = super(FlatBlockAdmin, self).get_form(request, obj, **kwargs)
        class MyFlatBlockForm(Form):
            def clean_named_url(self):
                data = self.cleaned_data.get('named_url')
                try:
                    if data:
                        urlresolvers.reverse(data)
                except urlresolvers.NoReverseMatch:
                    raise forms.ValidationError(u'This is not a valid URL.')
                else:
                    return data
        return MyFlatBlockForm

admin.site.register(FlatBlock, FlatBlockAdmin)
