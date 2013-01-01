import urllib2
import json
import time
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db import models
from valeur.models import Valeur
from cour.models import Cour
import time

class GoogleFinanceAPI:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="
    
    def get(self,symbol,exchange):
        url = self.prefix+"%s:%s"%(exchange,symbol)
        u = urllib2.urlopen(url)
        content = u.read()
        obj = json.loads(content[3:])
        return obj[0]


def get_value(value):
    c = GoogleFinanceAPI()
    print value.NomAction
    print value.Marche.Nom
    quote = c.get(value.NomAction,value.Marche.Nom)
    print quote
    print quote[u'lt'] 
    quote[u'lt'] = "%s "%quote[u'lt'] + time.strftime("%Y")
    try :
        cour = Cour.objects.get(Valeur=value,Prix=quote[u'l'],Date_Recup=quote[u'lt'],Variation=quote[u'c'])
    except :
       cour = Cour(Valeur=value,Prix=quote[u'l'],Date_Recup=quote[u'lt'],Variation=quote[u'c'])
       cour.save()
       time.sleep(30)
        
while 1 :
    valeurs =   Valeur.objects.all()
    for valeur in valeurs :
        v = get_value(valeur)
