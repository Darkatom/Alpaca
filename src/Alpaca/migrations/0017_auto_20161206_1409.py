# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Alpaca', '0016_auto_20161130_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='attendants_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='activity',
            name='city',
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
