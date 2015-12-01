# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0002_auto_20151027_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='athlete',
            name='first_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
