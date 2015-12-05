# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runleague', '0007_auto_20151203_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turn', models.IntegerField(default=0)),
                ('league', models.OneToOneField(to='runleague.League')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='team',
            name='draftpick',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='league',
            name='size',
            field=models.IntegerField(default=10, choices=[(8, 8), (10, 10), (12, 12)]),
            preserve_default=True,
        ),
    ]
