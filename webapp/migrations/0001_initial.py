# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('q_imporant_find_cancer', models.CharField(choices=[('Very Concerned', 'Very Concerned'), ('Somewhat Concerned', 'Somewhat Concerned'), ('Not Concerned', 'Not Concerned')], max_length=50)),
                ('q_concerned_false_alarm', models.CharField(choices=[('Very Concerned', 'Very Concerned'), ('Somewhat Concerned', 'Somewhat Concerned'), ('Not Concerned', 'Not Concerned')], max_length=50)),
                ('q_concerned_radiation', models.CharField(choices=[('Very Concerned', 'Very Concerned'), ('Somewhat Concerned', 'Somewhat Concerned'), ('Not Concerned', 'Not Concerned')], max_length=50)),
                ('q_concerned_unnecessary_treatment', models.CharField(choices=[('Very Concerned', 'Very Concerned'), ('Somewhat Concerned', 'Somewhat Concerned'), ('Not Concerned', 'Not Concerned')], max_length=50)),
                ('q_concerned_surgery', models.CharField(choices=[('Very Concerned', 'Very Concerned'), ('Somewhat Concerned', 'Somewhat Concerned'), ('Not Concerned', 'Not Concerned')], max_length=50)),
                ('q_talk_not_screened', models.CharField(choices=[('Yes', 'Yes, I want to talk about this'), ('No', 'No, I dont want to talk about this')], max_length=50)),
                ('q_talk_how_soon', models.CharField(choices=[('Yes', 'Yes, I want to talk about this'), ('No', 'No, I dont want to talk about this')], max_length=50)),
                ('q_talk_more_screening', models.CharField(choices=[('Yes', 'Yes, I want to talk about this'), ('No', 'No, I dont want to talk about this')], max_length=50)),
                ('q_talk_having_surgery', models.CharField(choices=[('Yes', 'Yes, I want to talk about this'), ('No', 'No, I dont want to talk about this')], max_length=50)),
                ('q_confirm', models.CharField(choices=[('quit smoking', 'The best thing to lower your risk of dying from lung cancer is to quit smoking or continue to not smoke.'), ('annual screening', 'I should return once a year for annual screening.')], max_length=50)),
            ],
        ),
    ]
