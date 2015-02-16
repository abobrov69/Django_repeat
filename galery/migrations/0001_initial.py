# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titel', models.CharField(max_length=256, verbose_name=b'Header')),
                ('dateiname_gross', models.CharField(max_length=64, verbose_name=b'Big image file name')),
                ('dateiname_klein', models.CharField(max_length=64, verbose_name=b'Small image file name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalerieSeite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seite_url', models.CharField(max_length=64, verbose_name=b'URL', blank=True)),
                ('titel', models.CharField(max_length=256, verbose_name=b'Header')),
                ('isdeleted', models.BooleanField(default=False)),
                ('text', models.TextField(verbose_name=b'Text', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='seite',
            field=models.ForeignKey(to='galery.GalerieSeite'),
            preserve_default=True,
        ),
    ]
