# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('runleague', '0005_league_draftdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='draftdate',
            new_name='draft_date_end',
        ),
        migrations.AddField(
            model_name='league',
            name='draft_date_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 16, 32, 17, 974000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
