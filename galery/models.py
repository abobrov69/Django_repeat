from django.db import models

class GalerieSeite(models.Model):
    seite_url = models.CharField(max_length=64, verbose_name= 'URL', blank=True)
    titel = models.CharField(max_length=256, verbose_name= 'Header')
    isdeleted = models.BooleanField(default=False)
    text = models.TextField(blank=True, verbose_name='Text')

    def __unicode__(self):
        return self.titel + '\n' + self.seite_url

    def delete(self, using=None):
        self.isdeleted = True
        self.save ()

class Bild(models.Model):
    seite = models.ForeignKey(GalerieSeite)
    titel = models.CharField(max_length=256, verbose_name= 'Header')
    dateiname_gross = models.CharField(max_length=64, verbose_name= 'Big image file name')
    dateiname_klein = models.CharField(max_length=64, verbose_name= 'Small image file name')
    isdeleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.titel + '\n' + self.dateiname_gross

    def delete(self, using=None):
        self.isdeleted = True
        self.save ()
