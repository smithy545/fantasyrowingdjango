# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=18, null=True)),
                ('height', models.FloatField(max_length=20, null=True, verbose_name=b'Height (cm)')),
                ('weight', models.IntegerField(null=True, verbose_name=b'Weight (kg)')),
                ('hometown', models.CharField(max_length=200, null=True)),
                ('high_school', models.CharField(max_length=200, null=True)),
                ('year', models.CharField(max_length=20, null=True)),
                ('major', models.CharField(max_length=200, null=True)),
                ('side', models.CharField(max_length=200, null=True)),
                ('ranking', models.IntegerField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('athletes', models.ManyToManyField(to='runleague.Athlete')),
                ('league', models.ForeignKey(to='runleague.League')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
