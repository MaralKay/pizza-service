# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-18 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=80)),
                ('customer_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('pizza_id', models.AutoField(primary_key=True, serialize=False)),
                ('pizza_size', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza'),
        ),
    ]
