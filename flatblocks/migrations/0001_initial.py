
from south.db import db
from django.db import models
from flatblocks.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'FlatBlock'
        db.create_table('flatblocks_flatblock', (
            ('id', orm['flatblocks.FlatBlock:id']),
            ('slug', orm['flatblocks.FlatBlock:slug']),
            ('header', orm['flatblocks.FlatBlock:header']),
            ('content', orm['flatblocks.FlatBlock:content']),
        ))
        db.send_create_signal('flatblocks', ['FlatBlock'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'FlatBlock'
        db.delete_table('flatblocks_flatblock')
        
    
    
    models = {
        'flatblocks.flatblock': {
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }
    
    complete_apps = ['flatblocks']
