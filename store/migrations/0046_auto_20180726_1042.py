# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-26 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0045_auto_20180726_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date_modified',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
