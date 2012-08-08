# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cour'
        db.create_table('cour_cour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Prix', self.gf('django.db.models.fields.FloatField')()),
            ('Date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Note', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal('cour', ['Cour'])

        # Adding M2M table for field Valeur on 'Cour'
        db.create_table('cour_cour_Valeur', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cour', models.ForeignKey(orm['cour.cour'], null=False)),
            ('valeur', models.ForeignKey(orm['valeur.valeur'], null=False))
        ))
        db.create_unique('cour_cour_Valeur', ['cour_id', 'valeur_id'])

        # Adding model 'Variation'
        db.create_table('cour_variation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Avant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Avant', to=orm['cour.Cour'])),
            ('Apres', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Apres', to=orm['cour.Cour'])),
            ('Variation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('cour', ['Variation'])


    def backwards(self, orm):
        # Deleting model 'Cour'
        db.delete_table('cour_cour')

        # Removing M2M table for field Valeur on 'Cour'
        db.delete_table('cour_cour_Valeur')

        # Deleting model 'Variation'
        db.delete_table('cour_variation')


    models = {
        'cour.cour': {
            'Date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Cour'},
            'Note': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'Prix': ('django.db.models.fields.FloatField', [], {}),
            'Valeur': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['valeur.Valeur']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cour.variation': {
            'Apres': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Apres'", 'to': "orm['cour.Cour']"}),
            'Avant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Avant'", 'to': "orm['cour.Cour']"}),
            'Meta': {'object_name': 'Variation'},
            'Variation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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

    complete_apps = ['cour']