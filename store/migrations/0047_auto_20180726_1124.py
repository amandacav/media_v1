# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-26 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0046_auto_20180726_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
