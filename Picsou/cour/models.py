from django.db import models

# Create your models here.

class Cour(models.Model):
    Prix = models.FloatField()
    Valeur = models.ForeignKey('valeur.Valeur',null=True, blank=True)
    Variation = models.TextField(max_length=1000, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Note = models.TextField(max_length=1000, null=True, blank=True)
    Date_Recup = models.TextField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return str(str(self.Date) + " "+ self.Valeur.Nom + " "  + str(self.Prix) )

class Variation(models.Model):
    Avant = models.ForeignKey('Cour',related_name='Avant')
    Apres = models.ForeignKey('Cour',related_name='Apres')
    Variation = models.FloatField(null=True, blank=True)