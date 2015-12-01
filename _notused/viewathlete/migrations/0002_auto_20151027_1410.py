# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete',
            old_name='athlete_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='athlete',
            old_name='athlete_name',
            new_name='name',
        ),
    ]
