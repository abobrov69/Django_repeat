from django.db import models

class GalerieSeite(models.Model):
    seite_url = models.CharField(max_length=64, verbose_name= 'URL', blank=True)
    titel = models.CharField(max_length=128, verbose_name= 'Header')
    isdeleted = models.BooleanField(default=False)
    text = models.TextField(blank=True, verbose_name='Text')
    dateiname_img = models.CharField(max_length=64, verbose_name= 'Image file name', default=' ')

    def __unicode__(self):
        return self.titel + '\n' + self.seite_url

    def delete(self, using=None):
        self.isdeleted = True
        self.save ()

class Bild(models.Model):
    seite = models.ForeignKey(GalerieSeite)
    titel = models.CharField(max_length=128, verbose_name= 'Header')
    dateiname_gross = models.CharField(max_length=64, verbose_name= 'Big image file name')
    dateiname_klein = models.CharField(max_length=64, verbose_name= 'Small image file name')
    kommentar = models.CharField(max_length=128, verbose_name= 'Comment', default=' ')
    isdeleted = models.IntegerField(default=0)
    sort_num = models.IntegerField(default=0)
    price = models.IntegerField (default=0)

    def __unicode__(self):
        return self.titel + '\n' + self.dateiname_gross + str(self.isdeleted)

    def delete(self, using=None):
        self.isdeleted = 1
        self.save ()
