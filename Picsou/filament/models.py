from django.db import models
# Create your models here.

class RatioAuteur(models.Model):
    Auteur = models.ForeignKey('tweet.Auteur')
    Ratio = models.FloatField()

Pertinence = (
(0,'Non'),
(1,'Oui'),
)

Avis = (
    (-1, 'Negatif'),
    (0, 'Neutre'),
    (1, 'Positif'),
)
class AnalyseTweet(models.Model):
    Tweet = models.ForeignKey('tweet.Tweet')
    AnalyseBot = models.IntegerField(choices=Avis,blank=True,null=True)
    AnalyseValideHumain = models.IntegerField(choices=Pertinence,blank=True,null=True)
    Final = models.IntegerField(choices=Avis,blank=True,null=True)
    Date = models.DateTimeField()
    Valeur = models.ForeignKey('valeur.Valeur')

class OldAnalyseTweet(models.Model): 
    Tweet = models.ForeignKey('tweet.Tweet')
    AnalyseBot = models.IntegerField(choices=Avis,blank=True,null=True)
    AnalyseValideHumain = models.IntegerField(choices=Pertinence,blank=True,null=True)
    Final = models.IntegerField(choices=Avis,blank=True,null=True)
    Pertinent = models.IntegerField(choices=Pertinence,blank=True,null=True)
    Date = models.DateTimeField()
    Valeur = models.ForeignKey('valeur.Valeur')   

class Prediction(models.Model):
    Valeur = models.ForeignKey('valeur.Valeur')
    Puissance =  models.FloatField()
    TweetAnalyse = models.ManyToManyField('AnalyseTweet')
    DateFait = models.DateTimeField()
    DatePrevu = models.DateTimeField()
    Pertinent = models.IntegerField(choices=Pertinence,blank=True,null=True)

class OldPrediction(models.Model):
    Valeur = models.ForeignKey('valeur.Valeur')
    Puissance =  models.FloatField()
    TweetAnalyse = models.ManyToManyField('OldAnalyseTweet')
    DateFait = models.DateTimeField()
    DatePrevu = models.DateTimeField()
    Pertinent = models.IntegerField(choices=Pertinence,blank=True,null=True)