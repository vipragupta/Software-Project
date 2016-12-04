# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='IS_Facutly_Selected',
            field=models.CharField(default=0, max_length=8, verbose_name='IS_Facutly_Selected'),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='IS_admin_Selected',
            field=models.CharField(default=0, max_length=8, verbose_name='IS_admin_Selected'),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='Student_Selected',
            field=models.CharField(default=0, max_length=20, verbose_name='Student ID'),
        ),
    ]
