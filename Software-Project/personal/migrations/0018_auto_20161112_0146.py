# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0017_auto_20161112_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='Min_GPA',
            field=models.FloatField(default='0', verbose_name='*GPA (Should be between 0 to 4)', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)]),
        ),
        migrations.AddField(
            model_name='student',
            name='Availability',
            field=models.CharField(default='none', max_length=60, verbose_name='', choices=[('1', 'True'), ('0', 'False')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Degree_Level',
            field=models.CharField(default='none', max_length=50, verbose_name='What degree are you pursuing?', choices=[('BS', 'BS'), ('MS', 'MS')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Enrollment',
            field=models.CharField(default='none', max_length=60, verbose_name='', choices=[('1', 'True'), ('0', 'False')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Got_DLA_Before',
            field=models.CharField(default='none', max_length=50, verbose_name='Have you worked for DLA before?', choices=[('1', 'True'), ('0', 'False')]),
            preserve_default=False,
        ),
    ]
