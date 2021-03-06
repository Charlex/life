# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_finances', '0005_auto_20151211_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=500),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=500),
        ),
    ]
