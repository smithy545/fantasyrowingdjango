# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('runleague', '0008_auto_20151204_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='athlete',
            options={'ordering': ['ranking']},
        ),
        migrations.RemoveField(
            model_name='league',
            name='draft_end_date',
        ),
        migrations.RemoveField(
            model_name='league',
            name='draft_start_date',
        ),
        migrations.AddField(
            model_name='schedule',
            name='draft_end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 1, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='draft_start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 5, 2, 39, 59, 212000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
