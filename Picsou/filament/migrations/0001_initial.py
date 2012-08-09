# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RatioAuteur'
        db.create_table('filament_ratioauteur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Auteur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweet.Auteur'])),
            ('Ratio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('filament', ['RatioAuteur'])

        # Adding model 'AnalyseTweet'
        db.create_table('filament_analysetweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Tweet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweet.Tweet'])),
            ('AnalyseBot', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('AnalyseValideHumain', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('Pertinent', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('Date', self.gf('django.db.models.fields.DateTimeField')()),
            ('Valeur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valeur.Valeur'])),
        ))
        db.send_create_signal('filament', ['AnalyseTweet'])

        # Adding model 'OldAnalyseTweet'
        db.create_table('filament_oldanalysetweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Tweet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweet.Tweet'])),
            ('AnalyseBot', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('AnalyseValideHumain', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('Pertinent', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('Date', self.gf('django.db.models.fields.DateTimeField')()),
            ('Valeur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valeur.Valeur'])),
        ))
        db.send_create_signal('filament', ['OldAnalyseTweet'])

        # Adding model 'Prediction'
        db.create_table('filament_prediction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Valeur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valeur.Valeur'])),
            ('Puissance', self.gf('django.db.models.fields.FloatField')()),
            ('DateFait', self.gf('django.db.models.fields.DateTimeField')()),
            ('DatePrevu', self.gf('django.db.models.fields.DateTimeField')()),
            ('Pertinent', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('filament', ['Prediction'])

        # Adding M2M table for field TweetAnalyse on 'Prediction'
        db.create_table('filament_prediction_TweetAnalyse', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('prediction', models.ForeignKey(orm['filament.prediction'], null=False)),
            ('analysetweet', models.ForeignKey(orm['filament.analysetweet'], null=False))
        ))
        db.create_unique('filament_prediction_TweetAnalyse', ['prediction_id', 'analysetweet_id'])

        # Adding model 'OldPrediction'
        db.create_table('filament_oldprediction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Valeur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valeur.Valeur'])),
            ('Puissance', self.gf('django.db.models.fields.FloatField')()),
            ('DateFait', self.gf('django.db.models.fields.DateTimeField')()),
            ('DatePrevu', self.gf('django.db.models.fields.DateTimeField')()),
            ('Pertinent', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('filament', ['OldPrediction'])

        # Adding M2M table for field TweetAnalyse on 'OldPrediction'
        db.create_table('filament_oldprediction_TweetAnalyse', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('oldprediction', models.ForeignKey(orm['filament.oldprediction'], null=False)),
            ('oldanalysetweet', models.ForeignKey(orm['filament.oldanalysetweet'], null=False))
        ))
        db.create_unique('filament_oldprediction_TweetAnalyse', ['oldprediction_id', 'oldanalysetweet_id'])


    def backwards(self, orm):
        # Deleting model 'RatioAuteur'
        db.delete_table('filament_ratioauteur')

        # Deleting model 'AnalyseTweet'
        db.delete_table('filament_analysetweet')

        # Deleting model 'OldAnalyseTweet'
        db.delete_table('filament_oldanalysetweet')

        # Deleting model 'Prediction'
        db.delete_table('filament_prediction')

        # Removing M2M table for field TweetAnalyse on 'Prediction'
        db.delete_table('filament_prediction_TweetAnalyse')

        # Deleting model 'OldPrediction'
        db.delete_table('filament_oldprediction')

        # Removing M2M table for field TweetAnalyse on 'OldPrediction'
        db.delete_table('filament_oldprediction_TweetAnalyse')


    models = {
        'filament.analysetweet': {
            'AnalyseBot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'AnalyseValideHumain': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Date': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'AnalyseTweet'},
            'Pertinent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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