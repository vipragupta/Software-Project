# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apprenticeship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=120)),
                ('Details', models.CharField(max_length=120)),
                ('Project_Link1', models.CharField(max_length=120)),
                ('Project_Link2', models.FileField(default='settings.MEDIA_ROOT/default/temp.txt', storage=django.core.files.storage.FileSystemStorage(location=b'./media'), upload_to='Apprenticeship')),
                ('Special_Requirements', models.CharField(max_length=120)),
                ('Departments', models.CharField(max_length=120, choices=[('Aerospace', 'Aerospace Engineering'), ('Applied Mathematics', 'Applied Mathematics'), ('Architectural', 'Architectural Engineering'), ('Chemical', 'Chemical Engineering'), ('Biological', 'Biological Engineering'), ('Civil', 'Civil Engineering'), ('Computer Science', 'Computer Science'), ('Electrical', 'Electrical Engineering'), ('Electrical and Computer', 'Electrical and Computer Engineering'), ('Egineering Physics', 'Engineering Physics'), ('Environmental', 'Environmental Engineering'), ('Mechanical', 'Mechanical Engineering'), ('Technology Arts and Media', 'Technology Arts and Media')])),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryFaculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_Name', models.CharField(max_length=120)),
                ('Last_Name', models.CharField(max_length=120)),
                ('Contact_Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Department', models.CharField(max_length=120, choices=[('Aerospace', 'Aerospace Engineering'), ('Applied Mathematics', 'Applied Mathematics'), ('Architectural', 'Architectural Engineering'), ('Chemical', 'Chemical Engineering'), ('Biological', 'Biological Engineering'), ('Civil', 'Civil Engineering'), ('Computer Science', 'Computer Science'), ('Electrical', 'Electrical Engineering'), ('Electrical and Computer', 'Electrical and Computer Engineering'), ('Egineering Physics', 'Engineering Physics'), ('Environmental', 'Environmental Engineering'), ('Mechanical', 'Mechanical Engineering'), ('Technology Arts and Media', 'Technology Arts and Media')])),
                ('Communities', models.CharField(max_length=120, choices=[('select1', 'Yes'), ('select2', 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='SecondFaculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_Name', models.CharField(max_length=120)),
                ('Last_Name', models.CharField(max_length=120)),
                ('Contact_Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Department', models.CharField(max_length=120, choices=[('Aerospace', 'Aerospace Engineering'), ('Applied Mathematics', 'Applied Mathematics'), ('Architectural', 'Architectural Engineering'), ('Chemical', 'Chemical Engineering'), ('Biological', 'Biological Engineering'), ('Civil', 'Civil Engineering'), ('Computer Science', 'Computer Science'), ('Electrical', 'Electrical Engineering'), ('Electrical and Computer', 'Electrical and Computer Engineering'), ('Egineering Physics', 'Engineering Physics'), ('Environmental', 'Environmental Engineering'), ('Mechanical', 'Mechanical Engineering'), ('Technology Arts and Media', 'Technology Arts and Media')])),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
