# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tp', '0004_auto_20170826_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
