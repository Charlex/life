# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_finances', '0007_auto_20151211_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='date_due',
            field=models.DateField(null=True),
        ),
    ]
