# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runleague', '0002_auto_20151130_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='leaguesize',
        ),
        migrations.AddField(
            model_name='league',
            name='size',
            field=models.IntegerField(default=8, choices=[(6, 6), (8, 8), (10, 10)]),
            preserve_default=True,
        ),
    ]
