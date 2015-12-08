# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0007_auto_20150703_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='bild',
            name='img_gross',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
        migrations.AddField(
            model_name='bild',
            name='img_klein',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
        migrations.AddField(
            model_name='galerieseite',
            name='img',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
    ]
