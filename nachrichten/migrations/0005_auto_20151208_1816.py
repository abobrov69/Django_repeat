# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nachrichten', '0004_auto_20151208_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='img_gross',
            field=models.ImageField(default=b'', upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='img_klein',
            field=models.ImageField(default=b'', upload_to=b'', blank=True),
        ),
    ]
