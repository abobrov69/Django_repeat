# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0005_auto_20150220_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='bild',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bild',
            name='sort_num',
            field=models.IntegerField(default=0),
        ),
    ]
