# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nachrichten', '0005_auto_20151208_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='titel',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
