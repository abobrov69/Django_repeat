# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0008_auto_20151208_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bild',
            name='img_gross',
            field=models.ImageField(default=b'', upload_to=b'', verbose_name=b'Big image file'),
        ),
        migrations.AlterField(
            model_name='bild',
            name='img_klein',
            field=models.ImageField(default=b'', upload_to=b'', verbose_name=b'Small image file'),
        ),
    ]
