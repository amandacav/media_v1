# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20170615_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
