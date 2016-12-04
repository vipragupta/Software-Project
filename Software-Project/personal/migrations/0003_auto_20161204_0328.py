# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20161204_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Project_selected_for',
        ),
        migrations.AlterField(
            model_name='student',
            name='First_Preference',
            field=models.CharField(max_length=200, verbose_name='*First Preference', choices=[('0', None), (b'14', '14:APPM - Machine Learning for earthquake prediction'), (b'15', '15:Merton\u2019s Problem with Human Capital Investment'), (b'16', '16:Autonomous Robotic Planetary Exploration Simulator'), (b'17', '17:GPS/GNSS Receiver Design/Development for Space Applications'), (b'18', '18:Throw Away Accounts'), (b'19', '19:Social norms in online communities'), (b'20', '20:Title')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='Five_Preference',
            field=models.CharField(max_length=200, verbose_name='Five Preference', choices=[('0', None), (b'14', '14:APPM - Machine Learning for earthquake prediction'), (b'15', '15:Merton\u2019s Problem with Human Capital Investment'), (b'16', '16:Autonomous Robotic Planetary Exploration Simulator'), (b'17', '17:GPS/GNSS Receiver Design/Development for Space Applications'), (b'18', '18:Throw Away Accounts'), (b'19', '19:Social norms in online communities'), (b'20', '20:Title')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='Four_Preference',
            field=models.CharField(max_length=200, verbose_name='Four Preference', choices=[('0', None), (b'14', '14:APPM - Machine Learning for earthquake prediction'), (b'15', '15:Merton\u2019s Problem with Human Capital Investment'), (b'16', '16:Autonomous Robotic Planetary Exploration Simulator'), (b'17', '17:GPS/GNSS Receiver Design/Development for Space Applications'), (b'18', '18:Throw Away Accounts'), (b'19', '19:Social norms in online communities'), (b'20', '20:Title')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='Three_Preference',
            field=models.CharField(max_length=200, verbose_name='Three Preference', choices=[('0', None), (b'14', '14:APPM - Machine Learning for earthquake prediction'), (b'15', '15:Merton\u2019s Problem with Human Capital Investment'), (b'16', '16:Autonomous Robotic Planetary Exploration Simulator'), (b'17', '17:GPS/GNSS Receiver Design/Development for Space Applications'), (b'18', '18:Throw Away Accounts'), (b'19', '19:Social norms in online communities'), (b'20', '20:Title')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='Two_Preference',
            field=models.CharField(max_length=200, verbose_name='Two Preference', choices=[('0', None), (b'14', '14:APPM - Machine Learning for earthquake prediction'), (b'15', '15:Merton\u2019s Problem with Human Capital Investment'), (b'16', '16:Autonomous Robotic Planetary Exploration Simulator'), (b'17', '17:GPS/GNSS Receiver Design/Development for Space Applications'), (b'18', '18:Throw Away Accounts'), (b'19', '19:Social norms in online communities'), (b'20', '20:Title')]),
        ),
    ]
