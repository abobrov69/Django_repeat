# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0006_auto_20150629_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bild',
            name='isdeleted',
            field=models.IntegerField(default=0),
        ),
    ]
