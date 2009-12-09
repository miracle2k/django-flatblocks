
from south.db import db
from django.db import models
from flatblocks.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'FlatBlock.url'
        db.add_column('flatblocks_flatblock', 'url', orm['flatblocks.flatblock:url'])
        
        # Adding field 'FlatBlock.named_url'
        db.add_column('flatblocks_flatblock', 'named_url', orm['flatblocks.flatblock:named_url'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'FlatBlock.url'
        db.delete_column('flatblocks_flatblock', 'url')
        
        # Deleting field 'FlatBlock.named_url'
        db.delete_column('flatblocks_flatblock', 'named_url')
        
    
    
    models = {
        'flatblocks.flatblock': {
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'named_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }
    
    complete_apps = ['flatblocks']
