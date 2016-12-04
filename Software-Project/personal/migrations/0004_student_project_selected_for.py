# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20161204_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Project_selected_for',
            field=models.IntegerField(default=0, verbose_name='Project ID'),
        ),
    ]
