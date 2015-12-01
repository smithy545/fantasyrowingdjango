# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0009_auto_20151028_1615'),
        ('viewteam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_ids',
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='team_members',
            field=models.ForeignKey(default='', to='viewathlete.Athlete'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
