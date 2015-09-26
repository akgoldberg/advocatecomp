# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'alumni_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('middleName', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('article', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('nickName', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('streetAddress1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('streetAddress2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('streetAddress3', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zipCode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('linkedIn', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('followed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('profession', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('graduationYear', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('otherDegrees', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('board', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('positionHeld', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('publishedWork', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('formCategory', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('dateAdded', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'alumni', ['User'])

        # Adding unique constraint on 'User', fields ['firstName', 'lastName']
        db.create_unique(u'alumni_user', ['firstName', 'lastName'])

        # Adding model 'Post'
        db.create_table(u'alumni_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.User'])),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('file_upload', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'alumni', ['Post'])


    def backwards(self, orm):
        # Removing unique constraint on 'User', fields ['firstName', 'lastName']
        db.delete_unique(u'alumni_user', ['firstName', 'lastName'])

        # Deleting model 'User'
        db.delete_table(u'alumni_user')

        # Deleting model 'Post'
        db.delete_table(u'alumni_post')


    models = {
        u'alumni.post': {
            'Meta': {'object_name': 'Post'},
            'file_upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['alumni.User']"})
        },
        u'alumni.user': {
            'Meta': {'ordering': "('firstName', 'lastName')", 'unique_together': "(['firstName', 'lastName'],)", 'object_name': 'User'},
            'article': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'board': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'positionHeld': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publishedWork': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'streetAddress1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'streetAddress2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'streetAddress3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'zipCode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['alumni']