# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20160726_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='q_confirm',
        ),
        migrations.AddField(
            model_name='survey',
            name='q_confirm_annual_screening',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='q_confirm_quit_smoking',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]