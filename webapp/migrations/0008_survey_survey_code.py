# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-07 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20160727_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='survey_code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
