# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AnalyseTweet.Pertinent'
        db.delete_column('filament_analysetweet', 'Pertinent')

        # Adding field 'AnalyseTweet.PertinentBot'
        db.add_column('filament_analysetweet', 'PertinentBot',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'AnalyseTweet.PertinentHumain'
        db.add_column('filament_analysetweet', 'PertinentHumain',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'AnalyseTweet.Pertinent'
        db.add_column('filament_analysetweet', 'Pertinent',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'AnalyseTweet.PertinentBot'
        db.delete_column('filament_analysetweet', 'PertinentBot')

        # Deleting field 'AnalyseTweet.PertinentHumain'
        db.delete_column('filament_analysetweet', 'PertinentHumain')


    models = {
        'filament.analysetweet': {
            'AnalyseBot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'AnalyseValideHumain': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Date': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'AnalyseTweet'},
            'PertinentBot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'PertinentHumain': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Tweet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tweet.Tweet']"}),
            'Valeur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['valeur.Valeur']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'filament.oldanalysetweet': {
            'AnalyseBot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'AnalyseValideHumain': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Date': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'OldAnalyseTweet'},
            'Pertinent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Tweet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tweet.Tweet']"}),
            'Valeur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['valeur.Valeur']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'filament.oldprediction': {
            'DateFait': ('django.db.models.fields.DateTimeField', [], {}),
            'DatePrevu': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'OldPrediction'},
            'Pertinent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Puissance': ('django.db.models.fields.FloatField', [], {}),
            'TweetAnalyse': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['filament.OldAnalyseTweet']", 'symmetrical': 'False'}),
            'Valeur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['valeur.Valeur']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'filament.prediction': {
            'DateFait': ('django.db.models.fields.DateTimeField', [], {}),
            'DatePrevu': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Prediction'},
            'Pertinent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Puissance': ('django.db.models.fields.FloatField', [], {}),
            'TweetAnalyse': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['filament.AnalyseTweet']", 'symmetrical': 'False'}),
            'Valeur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['valeur.Valeur']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'filament.ratioauteur': {
            'Auteur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tweet.Auteur']"}),
            'Meta': {'object_name': 'RatioAuteur'},
            'Ratio': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tweet.auteur': {
            'Amis': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tweet.Auteur']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Auteur'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Note': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tweet.hashtag': {
            'HahTag': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'HashTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tweet.tweet': {
            'Analyse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Auteur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tweet.Auteur']", 'null': 'True', 'blank': 'True'}),
            'Contenu': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'HasTag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tweet.HashTag']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Tweet'},
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

    complete_apps = ['filament']