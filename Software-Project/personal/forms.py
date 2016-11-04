from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.forms import AuthenticationForm 
from django import forms

from .models import *

#from .models import Student


class ProjectModelForm(forms.ModelForm):
    
    
    SF_First_Name = forms.CharField(required=False)
    SF_Last_Name = forms.CharField(required=False)
    SF_Contact_Number = forms.IntegerField(required=False)
    SF_Email = forms.EmailField(required=False)
    SF_Department = forms.ChoiceField(required=False,
        choices=DEPARTMENT
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
    Country = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), initial = "United States")
    Address_Line_2 = forms.CharField(required=False)
    Country = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), initial = "United States")
    SAddress_Line_2 = forms.CharField(label="Summer Address Line 2", required=False)
    SCountry = forms.CharField(label="Summer Country", widget=forms.TextInput(attrs={'readonly':'True'}), initial = "United States")
    Secondary_Major = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                choices=DEPARTMENT,
                                                label="Secondary Major", 
                                                required=False)
    Primary_Major = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                choices=DEPARTMENT,
                                                label="Primary Major")
    Previous_Research = forms.ChoiceField(label="Do you have previous research experience?", required=False, choices=TRUE_FALSE, widget=forms.RadioSelect)
    Applied_Before = forms.ChoiceField(label="*Have you had a background check yet (at CU)? If yes when? (Take your best guess if you aren't sure.)", choices=TRUE_FALSE_NS, widget=forms.RadioSelect)
    Background_check = forms.ChoiceField(label="*Have you had Discrimination and Harassment Awareness training yet (at CU)? If yes when? (Take your best guess if you aren't sure.)", choices=TRUE_FALSE_NS, widget=forms.RadioSelect)
    Discrimination_training = forms.ChoiceField(label="*Have you applied for Discovery Learning Apprenticeship before?", choices=TRUE_FALSE, widget=forms.RadioSelect)
    

    class Meta:
        model = Student
        fields = [
            "Student_Id",
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
            "Phone",
            "Email",
            "SAddress_Line_1",
            "SAddress_Line_2",
            "SCity",
            "SState",
            "SZip",
            "SCountry",
            "SPhone",
            "SEmail",
            "Primary_Major",
            "GPA",
            "Secondary_Major",
            "Level",
            "Anticipated_Graduation",
            "Previous_Research",
            "Applied_Before",
            "First_Preference",
            "Two_Preference",
            "Three_Preference",
            "Four_Preference",
            "Five_Preference",
            "Background_check",
            "Discrimination_training",
            "SSN"
        ]