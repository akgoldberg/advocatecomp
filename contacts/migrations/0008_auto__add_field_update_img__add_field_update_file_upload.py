# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Update.img'
        db.add_column(u'contacts_update', 'img',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Update.file_upload'
        db.add_column(u'contacts_update', 'file_upload',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Update.img'
        db.delete_column(u'contacts_update', 'img')

        # Deleting field 'Update.file_upload'
        db.delete_column(u'contacts_update', 'file_upload')


    models = {
        u'contacts.contact': {
            'Meta': {'ordering': "('firstName', 'lastName')", 'unique_together': "(['firstName', 'lastName'],)", 'object_name': 'Contact'},
            'article': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'board': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'donationBracket': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'followed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'formCategory': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'graduationYear': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'linkedIn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'middleName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nickName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'otherDegrees': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'positionHeld': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publishedWork': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'streetAddress1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'streetAddress2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'streetAddress3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'zipCode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'contacts.interaction': {
            'Meta': {'object_name': 'Interaction'},
            'category': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'donationAmount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {})
        },
        u'contacts.update': {
            'Meta': {'object_name': 'Update'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'file_upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['contacts']