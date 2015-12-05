# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('runleague', '0010_auto_20151204_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='draft_start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 5, 3, 7, 8, 409000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
