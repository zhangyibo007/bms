# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 09:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0013_auto_20160506_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamname',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 6, 9, 24, 21, 638321, tzinfo=utc)),
            preserve_default=False,
        ),
    ]