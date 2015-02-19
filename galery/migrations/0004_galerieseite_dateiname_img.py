# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0003_bild_isdeleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='galerieseite',
            name='dateiname_img',
            field=models.CharField(default=b' ', max_length=64, verbose_name=b'Image file name'),
            preserve_default=True,
        ),
    ]
