# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0009_auto_20151028_1615'),
        ('viewteam', '0002_auto_20151030_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_members',
        ),
        migrations.AddField(
            model_name='team',
            name='team_members',
            field=models.ManyToManyField(to='viewathlete.Athlete'),
        ),
    ]
