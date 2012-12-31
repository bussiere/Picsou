import urllib
import simplejson
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db import models
from tweet.models import Tweet
from valeur.models import Valeur
from tweet.models import Auteur
from tweet.models import HashTag
import tweepy
from django.utils.http import urlquote_plus

def searchTweets(query):
	auth = tweepy.BasicAuthHandler('Bot2bud','')
	api = tweepy.API(auth)
 	result = api.search(query)
 	print result
 	total = []
 	for r in result :
 		temp = {}
 		temp['from_user_name'] = urlquote_plus(r.from_user.encode('utf-8')).replace ("+"," ").replace("+%23","#").replace("%40","@").replace("%3A","")
 		temp['text'] = urlquote_plus(r.text.encode('utf-8')).replace ("+"," ").replace("%23","#").replace("%40","@").replace("%3A","")
 		print temp['from_user_name'] 
 		print temp['text']
 		total.append(temp)
 	return total
#return dict["results"]
 # for result in dict["results"]: # result is a list of dictionaries
 #  print result['from_user_name'].encode('utf-8'),"\n"
 #  print "*",result["text"].encode('utf-8'),"\n"

def traitementvaleur(valeur):
	result = {}
	result['Nom'] = searchTweets(valeur.Nom)
	result['NomAction']  = searchTweets(valeur.NomAction)
	count = 0
	for h in valeur.Hashtag.all() :
		result['Hashtag_%d'%count] = []
		result['Hashtag_%d'%count] = searchTweets("%s"%h.HashTag)
		count += 1
	for key in result.keys() :
		for r in result[key] :
			saveresult(r,key)

def extract_hash_tags(s):
	return set(part[1:] for part in s.split() if part.startswith('#'))


def saveresult(result,key):
	try :
		auteur = Auteur.objects.get(Nom=result['from_user_name'])
	except :
		auteur =  Auteur(Nom=result['from_user_name'])
		auteur.save()
	hashtags = extract_hash_tags(result["text"])
	

	tnom = Tweet(Auteur=auteur, Contenu=result["text"],Recherche=key)
	tnom.save()
	for h in hashtags :
		try :
			h1 = HashTag.objects.get(HashTag='#%s'%h)
		except :
			h1 = HashTag(HashTag='#%s'%h)
			h1.save()
		tnom.HashTag.add(h1)
	tnom.save()


valeurs =   Valeur.objects.all()
for valeur in valeurs :
	traitementvaleur(valeur)


# we will search tweets about "fc liverpool" football team
#results = 