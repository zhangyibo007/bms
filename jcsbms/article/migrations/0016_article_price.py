# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20160427_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]