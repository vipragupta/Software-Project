# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_student_project_selected_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='Student_Selected',
            field=models.CharField(choices=[('1', 'True'), ('0', 'False')], max_length=60, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='Degree_Level',
            field=models.CharField(choices=[('BS', 'BS'), ('MS', 'MS')], max_length=50, verbose_name='*What degree are you pursuing?'),
        ),
    ]
