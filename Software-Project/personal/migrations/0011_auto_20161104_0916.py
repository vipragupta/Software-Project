# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0010_auto_20161104_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Cover_Letter',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Resume',
        ),
    ]
