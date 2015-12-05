# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('runleague', '0009_auto_20151204_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='draft_end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 0, 0, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='draft_start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 5, 3, 4, 4, 514000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
