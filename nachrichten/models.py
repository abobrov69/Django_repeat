# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class Publication(models.Model):
    date = models.DateTimeField()
    titel = models.CharField(max_length=50, blank=True, verbose_name= u'Заголовок')
    text = models.CharField(max_length=250, verbose_name = u'Текст новости')
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL)
    isdeleted = models.BooleanField(default=False)
    img_gross = models.ImageField(default='', blank=True, verbose_name = u'Имя файла иллюстрации')
    img_klein = models.ImageField(default='', blank=True)
    url_bild_pg = models.CharField(max_length=250, blank=True)


    def __unicode__(self):
        return str(self.date) + '\n' + self.text

    def get_absolute_url(self):
        return reverse('blogclass') #, kwargs={'pk': self.pk})

    def delete(self, using=None):
        self.isdeleted = True
        self.save ()

    class Meta:
        ordering = ["-date"]

