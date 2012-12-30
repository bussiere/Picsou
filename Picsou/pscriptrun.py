import urllib
import simplejson
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db import models
from tweet.models import Tweet
from valeur.models import Valeur
from tweet.models import Auteur


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
	for key in result.keys() :
		saveresult(result[key],key)




def saveresult(result,key):
	try :
		Auteur = Auteur.objects.get(Nom=result['from_user_name'].encode('utf-8'))
	except :
		Auteur =  Auteur(Nom=result['from_user_name'].encode('utf-8'))
		Auteur.save()

	tnom = Tweet(Auteur=Auteur, Contenu=result["text"].encode('utf-8'))

valeurs =   Valeur.objects.all()
for valeur in valeurs :
	traitementvaleur(valeur)


# we will search tweets about "fc liverpool" football team
#results = 