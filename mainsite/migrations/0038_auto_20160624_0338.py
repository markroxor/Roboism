# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 22:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0037_auto_20160624_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='DOB',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 6, 23, 22, 8, 24, 732228, tzinfo=utc)),
        ),
    ]
