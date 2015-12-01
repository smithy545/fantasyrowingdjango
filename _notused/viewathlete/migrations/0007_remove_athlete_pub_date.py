# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewathlete', '0006_auto_20151028_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='pub_date',
        ),
    ]
