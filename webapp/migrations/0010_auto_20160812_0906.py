# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_survey_deccoach_harm_falsealarm_ptmentioned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='DecCoach_harm_falseAlarm_ptMentioned',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='q_concerned_radiation',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='q_concerned_surgery',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='q_talk_having_surgery',
        ),
        migrations.AddField(
            model_name='survey',
            name='d_focused_falsealarm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_focused_findcancer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_focused_overdx',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_focused_rad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_focused_surg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_harm_falsealarm_disc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_harm_falsealarm_ment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_harm_overdx_disc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_harm_overdx_ment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_harm_rad_disc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_harm_rad_ment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_harm_surg_disc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_harm_surg_ment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_keyMsg_quitsmoking',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_sure_bescreenedtoday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_sure_clearaboutbandh',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_sure_havesupport',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_sure_knowaboutbandh',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_sure_sureaboutbestchoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_talkabout_knowresults',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_talkabout_moretesting',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='d_talkabout_notscreening',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='q_concerned_rad',
            field=models.CharField(blank=True, choices=[('Very Concerned', 'Very Concerned'), ('Somewhat Concerned', 'Somewhat Concerned'), ('Not Concerned', 'Not Concerned')], max_length=50, null=True, verbose_name='being exposed to radiation from lung cancer?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='q_concerned_surg',
            field=models.CharField(blank=True, choices=[('Very Concerned', 'Very Concerned'), ('Somewhat Concerned', 'Somewhat Concerned'), ('Not Concerned', 'Not Concerned')], max_length=50, null=True, verbose_name='having surgery if lung cancer is found?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='q_talk_having_surg',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes, I want to talk about this'), ('No', 'No, I dont want to talk about this')], max_length=50, null=True, verbose_name='having surgery if lung cancer is found?'),
        ),
    ]
