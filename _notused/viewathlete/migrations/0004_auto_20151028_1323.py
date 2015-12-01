# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0003_auto_20151027_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 28, 17, 22, 43, 666000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='athlete',
            name='clubs',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='athlete',
            name='gender',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='athlete',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='athlete',
            name='residence',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='athlete',
            name='started_rowing',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='athlete',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='pub_date',
            field=models.DateField(auto_now=True, verbose_name=b'date published'),
        ),
    ]
