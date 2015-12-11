# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nachrichten', '0007_publication_url_bild_pg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.AlterField(
            model_name='publication',
            name='img_gross',
            field=models.ImageField(default=b'', upload_to=b'', verbose_name='\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430 \u0438\u043b\u043b\u044e\u0441\u0442\u0440\u0430\u0446\u0438\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='text',
            field=models.CharField(max_length=250, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='titel',
            field=models.CharField(max_length=50, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
