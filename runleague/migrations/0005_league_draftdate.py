# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('runleague', '0004_league_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='draftdate',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 0, 0)),
            preserve_default=False,
        ),
    ]
