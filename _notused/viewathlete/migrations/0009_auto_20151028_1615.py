# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0008_auto_20151028_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
