# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runleague', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='user',
        ),
        migrations.AddField(
            model_name='league',
            name='leaguesize',
            field=models.IntegerField(default=8),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='league',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='league',
            name='owner',
            field=models.ForeignKey(related_name='owner', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
