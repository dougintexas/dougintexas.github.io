# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20160812_0906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='d_keyMsg_quitsmoking',
            new_name='d_keymsg_quitsmoking',
        ),
    ]
