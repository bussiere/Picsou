import urllib
import simplejson
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db import models
from tweet.models import Tweet
from valeur.models import Valeur

def searchTweets(query):
 search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
 dict = simplejson.loads(search.read())
 return dict["results"]
 # for result in dict["results"]: # result is a list of dictionaries
 #  print result['from_user_name'].encode('utf-8'),"\n"
 #  print "*",result["text"].encode('utf-8'),"\n"

def traitementvaleur(valeur):
	result = {}
	result['Nom'] = searchTweets(valeur.Nom)
	result['NomAction']  = searchTweets(valeur.NomAction)
	result['Hashtag'] = []
	for h in valeur.Hashtag :
		result['Hashtag'].append(searchTweets("#%s"%h))



def saveresult(result):
	tnom = Tweet(Auteur=result['from_user_name'].encode('utf-8'), Contenu='')

valeurs =   Valeur.objects.all()
for valeur in valeurs :
	traitementvaleur(valeur)


# we will search tweets about "fc liverpool" football team
results = 