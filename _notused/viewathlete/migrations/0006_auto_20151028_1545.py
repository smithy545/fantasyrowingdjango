# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0005_auto_20151028_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='height',
            field=models.IntegerField(default=0, verbose_name=b'Height (cm)'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='weight',
            field=models.FloatField(default=0, verbose_name=b'Weight (kg)'),
        ),
    ]
