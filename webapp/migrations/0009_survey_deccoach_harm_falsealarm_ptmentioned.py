# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_survey_survey_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='DecCoach_harm_falseAlarm_ptMentioned',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
