# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 08:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_bannedword'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BannedWord',
        ),
    ]