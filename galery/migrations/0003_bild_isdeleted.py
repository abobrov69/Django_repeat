# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0002_auto_20150216_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='bild',
            name='isdeleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
