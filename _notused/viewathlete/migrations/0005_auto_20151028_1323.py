# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0004_auto_20151028_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='birth_date',
            field=models.DateField(),
        ),
    ]
