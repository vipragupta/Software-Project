from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your models here.
# MVC MODEL VIEW CONTROLLER

#NULL String
Empty = ""

#list of applicable departments
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


# Create your models here

class PrimaryFaculty(models.Model):
	First_Name = models.CharField("*First Name", max_length=120)#label="*First Name",required=True
	Last_Name = models.CharField("*Last Name", max_length=120)#label="*Last Name",required=True
	Contact_Number = models.IntegerField("*Contact Number")#label="*Contact Number",required=True
	Email = models.EmailField("*Email")#label="*Email",required=True
	Department = models.CharField("*Department", max_length=120, choices=DEPARTMENT)#, required=True, label="*Department"
	DEVELOPING_COMMUNITIES=[('select1','Yes'),('select2','No')]
	Communities = models.CharField("Does the project have focus on Engineering for developing communities?", max_length=120, choices=DEVELOPING_COMMUNITIES)#, label="Does the project have focus on Engineering for developing communities?"

	def __unicode__(self):
		return self.Email

	def __str__(self):
		return self.Email
    
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.Email})
	
	def GetList(self):
		return [self.First_Name, self.Last_Name, self.Contact_Number, self.Email, self.Department, self.DEVELOPING_COMMUNITIES, self.Communities]
  
class SecondFaculty(models.Model):
	First_Name = models.CharField(max_length=120)#label="First Name",, required=False
	Last_Name = models.CharField(max_length=120)#label="Last Name",, required=False
	Contact_Number = models.IntegerField()#label="Contact Number",required=False
	Email = models.EmailField()#label="Email",required=False
	Department = models.CharField(max_length=120, choices=DEPARTMENT )#, required=False, label="*Department"
    
	def __unicode__(self):
		return self.Email

	def __str__(self):
		return self.Email
    
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.Email})
  
class Apprenticeship(models.Model):
	Title = models.CharField(max_length=120)#label="*Apprenticeship Title",required=True
	Details = models.CharField("*Project Details (in brief)", max_length=120)#label="*Project Details (in brief)",required=True
	Project_Link1 = models.CharField("Link to Project Details", max_length=120)#, default=FRESHMAN)#label="Link to Project Details",required=False
	Project_Link2 = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='Apprenticeship', default='settings.MEDIA_ROOT/default/temp.txt')#label="File Upload (A file containing project details)",required=False
	Special_Requirements = models.CharField("Special skillset required", max_length=120)#label="Special skillset required",required=True
	Departments = models.CharField(max_length=120, choices=DEPARTMENT)#choices=DEPARTMENT, widget=forms.CheckboxSelectMultiple, label="Students should be enrolled in thw following departments only"
	PrimaryFaculty = models.CharField(max_length=120, default="")#label="FacultyEmail",required=True
	SecondaryFaculty = models.CharField(max_length=120, default="")#label="FacultyEmail",required=False, defalt = Empty
     
	def __unicode__(self):
		return self.Title

	def __str__(self):
		return self.Title
    
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.Title})    

	def SetPrimaryFaculty(self, id):
		self.PrimaryFaculty = id    
  
	def SetSecondaryFaculty(self, id):
		self.SecondaryFaculty = id

	def GetList(self):
		return [self.Title.encode('ascii','ignore'), self.Details.encode('ascii','ignore'), self.Departments.encode('ascii','ignore'), self.Special_Requirements.encode('ascii','ignore'), self.PrimaryFaculty.encode('ascii','ignore')]