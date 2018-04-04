# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_inventory_container'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='inventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Inventory'),
        ),
    ]
