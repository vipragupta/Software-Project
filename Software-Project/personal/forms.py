from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.forms import AuthenticationForm 
from django import forms

from .models import ProjectModel

from .models import Student


class ProjectModelForm(forms.ModelForm):
    
    
    SF_First_Name = forms.CharField(required=False)
    SF_Last_Name = forms.CharField(required=False)
    SF_Contact_Number = forms.IntegerField(required=False)
    SF_Email = forms.EmailField(required=False)
    SF_Department = forms.ChoiceField(required=False,
        choices=ProjectModel.DEPARTMENT
    )
    Appr_Project_Link1 = forms.CharField(required=False)
    Appr_Project_Link2 = forms.FileField(required=False)
    #Appr_Departments = forms.MultipleChoiceField(
    #    widget=forms.CheckboxSelectMultiple,
    #    choices=ProjectModel.DEPARTMENT,
    #)
    
    class Meta:
        model = ProjectModel
        fields = [
           "PF_First_Name",
        	"PF_Last_Name",
        	"PF_Contact_Number",
        	"PF_Email",
        	"PF_Department",
        	"PF_Communities",
        	"SF_First_Name",
        	"SF_Last_Name",
        	"SF_Contact_Number",
        	"SF_Email",
        	"SF_Department",
        	"Appr_Title",
        	"Appr_Details",
        	"Appr_Project_Link1",
        	"Appr_Project_Link2",
        	"Appr_Special_Requirements",
        	"Appr_Departments",
        	"Appr_Supervision_Level",
        	"Appr_Supervision_By",
        	"Appr_Nature_Of_Work",
         	"Appr_Prior_Work"
        ]

class StudentForm(forms.ModelForm):
	Gender = forms.ChoiceField(choices=Student.GENDER_CHOICES, widget=forms.RadioSelect)
	Race = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=Student.RACE_CHOICES,
    )
	Address_Line_2 = forms.CharField(required=False)
	class Meta:
		model = Student
		fields = [
			"First_Name",
			"Last_Name",
			"Gender",
			"Race",
			"Address_Line_1",
			"Address_Line_2",
			"City",
			"State",
			"Zip",
			"Country",
		]
