# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runleague', '0003_auto_20151201_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='open',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
