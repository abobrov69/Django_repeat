from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class Publication(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=140)
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL)
    isdeleted = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.date) + '\n' + self.text

    def get_absolute_url(self):
        return reverse('blogclass') #, kwargs={'pk': self.pk})

    def delete(self, using=None):
        self.isdeleted = True
        self.save ()

    class Meta:
        ordering = ["-date"]

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField()

    def __unicode__(self):
        return str(self.name)