import urllib
import simplejson
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# # settings.py
# from django.conf import settings

# settings.configure(

# DATABASE_ENGINE    = "django.db.backends.sqlite3",
# DATABASE_NAME      = "picsou.db",
# DATABASE_USER      = "",
# DATABASE_PASSWORD  = "",
# DATABASE_HOST      = "",
# DATABASE_PORT      = "",
# INSTALLED_APPS     = ("tweet","valeur")
# )
# from django.core.management import setup_environ
# setup_environ(settings)
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
	pass

valeurs =   Valeur.objects.all()
print valeurs
# we will search tweets about "fc liverpool" football team
results = searchTweets("#apple")