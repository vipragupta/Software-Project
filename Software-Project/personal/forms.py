from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.core.validators import MaxValueValidator
from .models import *

#from .models import Student


class ProjectModelForm(forms.ModelForm):
    
    
    SF_First_Name = forms.CharField(label="Second Faculty First Name",required=False)
    SF_Last_Name = forms.CharField(label="Second Faculty Last Name",required=False)
    SF_Contact_Number = forms.IntegerField(label="Second Faculty Contact Number",required=False)
    SF_Email = forms.EmailField(label="Second Faculty Email",required=False)
    SF_Department = forms.ChoiceField(label="Second Faculty Department",required=False,
        choices=DEPARTMENT
    )
    Appr_Project_Link1 = forms.CharField(required=False)
    Appr_Project_Link2 = forms.FileField(required=False)
    #Min_GPA = forms.CharField(label="Minimum GPA Required", required=False)
    Requirement1 = forms.CharField(label="Requirement I", required=False)
    Requirement2 = forms.CharField(label="Requirement II", required=False)
    Requirement3 = forms.CharField(label="Requirement III", required=False)

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
         	"Appr_Prior_Work",
            "Min_GPA",
            "Requirement1",
            "Requirement2",
            "Requirement3",            
        ]

class StudentForm(forms.ModelForm):
    Student_Id = forms.IntegerField(label="*Student Id", validators=[MaxValueValidator(9999999999)])
    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    Race = forms.ChoiceField(required=False,
            choices=RACE_CHOICES
    )
    
    Address_Line_2 = forms.CharField(required=False)
    Country = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}), initial = "United States")
    SAddress_Line_1 = forms.CharField(label="Summer Address Line 1",required=False)
    SAddress_Line_2 = forms.CharField(label="Summer Address Line 2", required=False)
    SCity = forms.CharField(label="Summer City", required=False)
    SState = forms.ChoiceField(label="Summer State", required=False, choices=US_STATES, initial={'NN': ''})
    SZip = forms.CharField(label="Summer Zip",required=False)
    Phone = forms.IntegerField(label="*Phone", validators=[MaxValueValidator(9999999999)])
    SPhone = forms.IntegerField(label="Summer Phone", validators=[MaxValueValidator(9999999999)],required=False)
    SEmail = forms.CharField(label="Summer Email", required=False)
    SCountry = forms.CharField(label="Summer Country", widget=forms.TextInput(attrs={'readonly':'True'}), initial = "United States")
    Secondary_Major = forms.ChoiceField(choices=DEPARTMENT, label="Secondary Major", required=False)
    #Primary_Major = forms.ChoiceField(choices=DEPARTMENT, label="Primary Major")
    Previous_Research = forms.ChoiceField(label="Do you have previous research experience?", required=False, choices=TRUE_FALSE, widget=forms.RadioSelect)
    Availability = forms.ChoiceField(label="*Will you be available for full year?", choices=TRUE_FALSE, widget=forms.RadioSelect)
    Applied_Before = forms.ChoiceField(label="*Have you had a background check yet (at CU)? If yes when? (Take your best guess if you aren't sure.)", choices=TRUE_FALSE_NS, widget=forms.RadioSelect)
    Got_DLA_Before = forms.ChoiceField(label="*Have you worked for DLA before?", choices=TRUE_FALSE, widget=forms.RadioSelect)
    Enrollment = forms.ChoiceField(label="*Are you enrolled in College of Engineering and Applied Science?", choices=TRUE_FALSE, widget=forms.RadioSelect)
    Background_check = forms.ChoiceField(required=False,label="*Have you had Discrimination and Harassment Awareness training yet (at CU)? If yes when? (Take your best guess if you aren't sure.)", choices=TRUE_FALSE_NS, widget=forms.RadioSelect)
    Discrimination_training = forms.ChoiceField(required=False,label="*Have you applied for Discovery Learning Apprenticeship before?", choices=TRUE_FALSE, widget=forms.RadioSelect)
    Skills = forms.CharField(label="Please list the three skills or qualifications that you feel make you a great candidate for the positions you selected. (Could be knowledge of a programming language, knowledge of a field, courses taken, personal characteristics, etc. If appropriate, note your match to requirements in job description. Please note responses are limited to 75 characters.)",widget=forms.TextInput(attrs={'readonly':'True'}), initial = "Please fill in the following fields")
    Skills_1 = forms.CharField(label="1.",required=False)
    Skills_2 = forms.CharField(label="2.",required=False)
    Skills_3 = forms.CharField(label="3.",required=False)
    Upload = forms.CharField(label="To complete the application, you must submit a resume and a cover letter. You can submit both using the form below. Please use either the pdf format or a text document. To improve your chances of being selected for an apprenticeship, please take the time to construct a well-written cover letter and resume.",widget=forms.TextInput(attrs={'readonly':'True'}), initial = "Please upload in the following fields")

    Two_Preference = forms.ChoiceField(label="Second Preference", required=False, choices=Student.PROJECTS)
    Three_Preference = forms.ChoiceField(label="Third Preference", required=False, choices=Student.PROJECTS)
    Four_Preference = forms.ChoiceField(label="Fourth Preference", required=False, choices=Student.PROJECTS)
    Five_Preference = forms.ChoiceField(label="Fifth Preference", required=False, choices=Student.PROJECTS)
    SSN=forms.IntegerField(label="*Last four digits of your Social Security Number: (this will only be used to acess your background check information)", validators=[MaxValueValidator(9999)])

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
            "Degree_Level",
            "Level",
            "Anticipated_Graduation",
            "Previous_Research",
            "Availability",
            "Applied_Before",
            "Got_DLA_Before",
            "First_Preference",
            "Two_Preference",
            "Three_Preference",
            "Four_Preference",
            "Five_Preference",
            "Background_check",
            "Discrimination_training",
            "SSN",
            "Enrollment",
            "Skills",
            "Skills_1",
            "Skills_2",
            "Skills_3",
            "Upload",
            #"Resume",
            #"Cover_Letter"
        ]
        
class UpdateReqForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			"P1_Req1",
			"P1_Req2",
			"P1_Req3",
			"P2_Req1",
			"P2_Req2",
			"P2_Req3",
			"P3_Req1",
			"P3_Req2",
			"P3_Req3",
			"P4_Req1",
			"P4_Req2",
			"P4_Req3",
			"P5_Req1",
			"P5_Req2",
			"P5_Req3",
			]
			
	def setlabel(self, labelname, labelvalue):
	    self.fields[labelname].label = labelvalue
        
class MyuserForm(forms.ModelForm):
    
    class Meta:
        model = Myuser
        fields = [
           "user",
        	"role",
        	"uid"
        ]