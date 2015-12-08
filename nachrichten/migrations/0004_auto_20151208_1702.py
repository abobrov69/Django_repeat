# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nachrichten', '0003_auto_20151208_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='img_gross',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
        migrations.AddField(
            model_name='publication',
            name='img_klein',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
    ]
