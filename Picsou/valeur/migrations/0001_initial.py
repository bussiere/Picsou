# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Valeur'
        db.create_table('valeur_valeur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=50, null=True, blank=True)),
            ('NomAction', self.gf('django.db.models.fields.TextField')(max_length=50, null=True, blank=True)),
            ('Note', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal('valeur', ['Valeur'])

        # Adding M2M table for field Hashtag on 'Valeur'
        db.create_table('valeur_valeur_Hashtag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('valeur', models.ForeignKey(orm['valeur.valeur'], null=False)),
            ('hashtag', models.ForeignKey(orm['tweet.hashtag'], null=False))
        ))
        db.create_unique('valeur_valeur_Hashtag', ['valeur_id', 'hashtag_id'])


    def backwards(self, orm):
        # Deleting model 'Valeur'
        db.delete_table('valeur_valeur')

        # Removing M2M table for field Hashtag on 'Valeur'
        db.delete_table('valeur_valeur_Hashtag')


    models = {
        'tweet.hashtag': {
            'HahTag': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'HashTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'valeur.valeur': {
            'Hashtag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tweet.HashTag']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Valeur'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'NomAction': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Note': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['valeur']