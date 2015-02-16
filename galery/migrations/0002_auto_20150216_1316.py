# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bild',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titel', models.CharField(max_length=256, verbose_name=b'Header')),
                ('dateiname_gross', models.CharField(max_length=64, verbose_name=b'Big image file name')),
                ('dateiname_klein', models.CharField(max_length=64, verbose_name=b'Small image file name')),
                ('seite', models.ForeignKey(to='galery.GalerieSeite')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='seite',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
