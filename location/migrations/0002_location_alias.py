# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='alias',
            field=models.CharField(default='Home', max_length=100),
            preserve_default=False,
        ),
    ]
