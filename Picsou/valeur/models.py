from django.db import models

class Marche(models.Model):
    Nom = models.TextField(max_length=50, null=True, blank=True)
    def __unicode__(self):
        return self.Nom

# Create your models here.
class Valeur(models.Model):
    Nom = models.TextField(max_length=50, null=True, blank=True)
    NomAction = models.TextField(max_length=50, null=True, blank=True)
    Hashtag = models.ManyToManyField('tweet.HashTag',null=True, blank=True)
    MotClef = models.ManyToManyField('tweet.MotClef',null=True, blank=True)
    Note = models.TextField(max_length=1000, null=True, blank=True)
    Marche = models.ForeignKey(Marche,unique=False, null=True, blank=True)
    def __unicode__(self):
        return self.Nom