# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-19 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_order_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='pizza_flavor',
            field=models.CharField(default='Surprise', max_length=100),
        ),
    ]
