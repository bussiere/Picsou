# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Auteur'
        db.create_table('tweet_auteur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=50, null=True, blank=True)),
            ('Note', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('tweet', ['Auteur'])

        # Adding M2M table for field Amis on 'Auteur'
        db.create_table('tweet_auteur_Amis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_auteur', models.ForeignKey(orm['tweet.auteur'], null=False)),
            ('to_auteur', models.ForeignKey(orm['tweet.auteur'], null=False))
        ))
        db.create_unique('tweet_auteur_Amis', ['from_auteur_id', 'to_auteur_id'])

        # Adding model 'HashTag'
        db.create_table('tweet_hashtag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('HahTag', self.gf('django.db.models.fields.TextField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('tweet', ['HashTag'])

        # Adding model 'Tweet'
        db.create_table('tweet_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Auteur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweet.Auteur'], null=True, blank=True)),
            ('Contenu', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('Analyse', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('tweet', ['Tweet'])

        # Adding M2M table for field HasTag on 'Tweet'
        db.create_table('tweet_tweet_HasTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tweet', models.ForeignKey(orm['tweet.tweet'], null=False)),
            ('hashtag', models.ForeignKey(orm['tweet.hashtag'], null=False))
        ))
        db.create_unique('tweet_tweet_HasTag', ['tweet_id', 'hashtag_id'])

        # Adding model 'OldTweet'
        db.create_table('tweet_oldtweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Auteur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweet.Auteur'], null=True, blank=True)),
            ('Contenu', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('Analyse', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('tweet', ['OldTweet'])

        # Adding M2M table for field HasTag on 'OldTweet'
        db.create_table('tweet_oldtweet_HasTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('oldtweet', models.ForeignKey(orm['tweet.oldtweet'], null=False)),
            ('hashtag', models.ForeignKey(orm['tweet.hashtag'], null=False))
        ))
        db.create_unique('tweet_oldtweet_HasTag', ['oldtweet_id', 'hashtag_id'])


    def backwards(self, orm):
        # Deleting model 'Auteur'
        db.delete_table('tweet_auteur')

        # Removing M2M table for field Amis on 'Auteur'
        db.delete_table('tweet_auteur_Amis')

        # Deleting model 'HashTag'
        db.delete_table('tweet_hashtag')

        # Deleting model 'Tweet'
        db.delete_table('tweet_tweet')

        # Removing M2M table for field HasTag on 'Tweet'
        db.delete_table('tweet_tweet_HasTag')

        # Deleting model 'OldTweet'
        db.delete_table('tweet_oldtweet')

        # Removing M2M table for field HasTag on 'OldTweet'
        db.delete_table('tweet_oldtweet_HasTag')


    models = {
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
        'tweet.oldtweet': {
            'Analyse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Auteur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tweet.Auteur']", 'null': 'True', 'blank': 'True'}),
            'Contenu': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'HasTag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tweet.HashTag']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'OldTweet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tweet.tweet': {
            'Analyse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Auteur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tweet.Auteur']", 'null': 'True', 'blank': 'True'}),
            'Contenu': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'HasTag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tweet.HashTag']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Tweet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tweet']