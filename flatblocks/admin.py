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
                if 'named_url' in self.cleaned_data:
                    data = self.cleaned_data['named_url']
                    try:
                        urlresolvers.reverse(data)
                    except urlresolvers.NoReverseMatch:
                        raise forms.ValidationError(u'This is not a valid URL.')
                    else:
                        return data
        return MyFlatBlockForm

admin.site.register(FlatBlock, FlatBlockAdmin)
