# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nachrichten', '0006_auto_20151210_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='url_bild_pg',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]
