# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runleague', '0006_auto_20151203_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='draft_date_end',
            new_name='draft_end_date',
        ),
        migrations.RenameField(
            model_name='league',
            old_name='draft_date_start',
            new_name='draft_start_date',
        ),
    ]
