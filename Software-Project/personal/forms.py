from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.forms import AuthenticationForm 
from django import forms

from .models import PrimaryFaculty
from .models import SecondFaculty
from .models import Apprenticeship
from .models import Student

#list of applicable departments - global variable
DEPARTMENT = [ 
	('Aerospace', 'Aerospace Engineering'),
	('Applied Mathematics', 'Applied Mathematics'),
	('Architectural', 'Architectural Engineering'),
	('Chemical', 'Chemical Engineering'),
	('Biological', 'Biological Engineering'),
	('Civil', 'Civil Engineering'),
	('Computer Science', 'Computer Science'),
	('Electrical', 'Electrical Engineering'),
	('Electrical and Computer', 'Electrical and Computer Engineering'),
	('Egineering Physics', 'Engineering Physics'),
	('Environmental', 'Environmental Engineering'),
    ('Mechanical', 'Mechanical Engineering'),
    ('Technology Arts and Media', 'Technology Arts and Media'),
	]

#Django forms are created below	
'''
class PrimaryFacultyForm(forms.Form):
	First_Name = forms.CharField(label="*First Name",required=True)
	Last_Name = forms.CharField(label="*Last Name",required=True)
	Contact_Number = forms.IntegerField(label="*Contact Number",required=True)
	Email = forms.EmailField(label="*Email",required=True)
	Department = forms.ChoiceField(choices=DEPARTMENT, required=True, label="*Department")
	
	DEVELOPING_COMMUNITIES=[('select1','Yes'),('select2','No')]

	Communities = forms.ChoiceField(choices=DEVELOPING_COMMUNITIES, label="Does the project have focus on Engineering for developing communities?")
'''

class PrimaryFacultyForm(forms.ModelForm):
    class Meta:
        model = PrimaryFaculty
        fields = [
            "First_Name",
            "Last_Name",
            "Contact_Number",
            "Email",
            "Department",
            "Communities",
        ]
        
'''
class SecondFacultyForm(forms.Form):
	First_Name = forms.CharField(label="First Name",required=False)
	Last_Name = forms.CharField(label="Last Name",required=False)
	Contact_Number = forms.IntegerField(label="Contact Number",required=False)
	Email = forms.EmailField(label="Email",required=False)
	Department = forms.ChoiceField(choices=DEPARTMENT, required=False, label="*Department" )
'''
class SecondFacultyForm(forms.ModelForm):
    class Meta:
        model = SecondFaculty
        fields = [
            "First_Name",
            "Last_Name",
            "Contact_Number",
            "Email",
            "Department"
        ]

'''
class ApprenticeshipForm(forms.Form):
	Title = forms.CharField(label="*Apprenticeship Title",required=True)
	Details = forms.CharField(label="*Project Details (in brief)",required=True)
	Project_Link1 = forms.CharField(label="Link to Project Details",required=False)
	Project_Link2 = forms.FileField(label="File Upload (A file containing project details)",required=False)
	Special_Requirements = forms.CharField(label="Special skillset required",required=True)
	Departments = forms.MultipleChoiceField(choices=DEPARTMENT, widget=forms.CheckboxSelectMultiple, label="Students should be enrolled in thw following departments only")
'''

class ApprenticeshipForm(forms.ModelForm):
    class Meta:
        model = Apprenticeship
        fields = [
            "Title",
            "Details",
            "Project_Link1",
            "Project_Link2",
            "Special_Requirements",
            "Departments"
        ]

class StudentForm(forms.ModelForm):
	#Gender = forms.CharField(choices=Student.CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Student
        fields = [
            "First_Name",
            "Last_Name",
            "Gender",
            "Address_Line_1",
            "Address_Line_2",
            "City",
            "State",
            "Zip",
            "Country",
        ]
