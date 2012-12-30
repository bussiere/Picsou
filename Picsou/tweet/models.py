from django.db import models

# Create your models here.

class Auteur(models.Model):
    Nom = models.TextField(max_length=50, null=True, blank=True)
    Note = models.TextField(max_length=1024, null=True, blank=True)
    Amis = models.ManyToManyField('Auteur',null=True, blank=True)
    Puissance =  models.FloatField()
    def __unicode__(self):
        return str(self.Nom)
    
class HashTag(models.Model):
    HahTag = models.TextField(max_length=50, null=True, blank=True)
    def __unicode__(self):
        return str(self.HahTag)

class MotClef(models.Model):
    MotClef = models.TextField(max_length=50, null=True, blank=True)
    def __unicode__(self):
        return str(self.MotClef)

class Tweet(models.Model):
    Auteur = models.ForeignKey(Auteur, unique=False, null=True, blank=True)
    Contenu = models.TextField(max_length=200, null=True, blank=True)
    Analyse = models.BooleanField(default=False)
    HasTag = models.ManyToManyField('HashTag')
    Salt = models.TextField(max_length=200, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Recherche = models.TextField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return str(self.Auteur + " "+ self.Contenu)

class OldTweet(models.Model):
    Auteur = models.ForeignKey(Auteur, unique=False, null=True, blank=True)
    Contenu = models.TextField(max_length=200, null=True, blank=True)
    Analyse = models.BooleanField(default=False)
    HasTag = models.ManyToManyField('HashTag')
    Salt = models.TextField(max_length=200, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Recherche = models.TextField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return str(self.Auteur + " "+ self.Contenu)