# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0004_galerieseite_dateiname_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='bild',
            name='kommentar',
            field=models.CharField(default=b' ', max_length=128, verbose_name=b'Comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bild',
            name='titel',
            field=models.CharField(max_length=128, verbose_name=b'Header'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='galerieseite',
            name='titel',
            field=models.CharField(max_length=128, verbose_name=b'Header'),
            preserve_default=True,
        ),
    ]
