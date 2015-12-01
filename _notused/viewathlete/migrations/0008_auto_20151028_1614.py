# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0007_remove_athlete_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='age',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='clubs',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='height',
            field=models.IntegerField(null=True, verbose_name=b'Height (cm)'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='residence',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='started_rowing',
            field=models.IntegerField(default=2000, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='weight',
            field=models.FloatField(null=True, verbose_name=b'Weight (kg)'),
        ),
    ]
