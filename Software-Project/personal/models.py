from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your models here.

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

class ProjectModel(models.Model):
	Id = models.AutoField(primary_key=True)
	
	#not required
	PF_First_Name = models.CharField("*First Name", max_length=120)
	PF_Last_Name = models.CharField("*Last Name", max_length=120)
	PF_Contact_Number = models.IntegerField("*Contact Number")
	PF_Email = models.EmailField("*Email")
	PF_Department = models.CharField("*Department", max_length=120, choices=DEPARTMENT)
	PF_DEVELOPING_COMMUNITIES=[('select1','Yes'),('select2','No')]
	PF_Communities = models.CharField("*Does the project have focus on Engineering for developing communities?", max_length=120, choices=PF_DEVELOPING_COMMUNITIES)
	
	SF_First_Name = models.CharField("Secondary Faculty, Firstname", max_length=120)
	SF_Last_Name = models.CharField("Secondary Faculty, Lastname", max_length=120)
	SF_Contact_Number = models.IntegerField(null=True, blank=True, default = 0)
	SF_Email = models.EmailField()
	SF_Department = models.CharField(max_length=120, choices=DEPARTMENT)
	
	Appr_Title = models.CharField("*Apprenticeship Title", max_length=120)
	Appr_Details = models.CharField("*Project Details (in brief)", max_length=2000)
	Appr_Project_Link1 = models.CharField("Link to Project Details", max_length=120)
	Appr_Project_Link2 = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='Apprenticeship', default='settings.MEDIA_ROOT/default/temp.txt')
	Appr_Special_Requirements = models.CharField("*Special skillset required", max_length=120)
	#need to split these things, based on comma
	Appr_Departments = models.CharField(max_length=120, choices=DEPARTMENT)#multiple widgets
	
	
	#make multiple
	APPR_SUPERVISION_LEVEL =[
		("None", "Very little supervision; student will need to work largely independently"),
		("Moderate", "Moderate amount of supervision and interaction with others"),
		("A lot", "Good deal of supervision; student will work as an integral part of a research team")
	]
 	Appr_Supervision_Level = models.CharField("*Supervision Level", max_length=180, choices=APPR_SUPERVISION_LEVEL)
	
	#Supervision provided by
	APPR_SUPERVISION_BY = [
		("Faculty", "Supervision primarily by faculty supervisor"),
		("Graduate Student", "Supervision primarily by graduate students"),
		("Combination", "Supervision primarily a combination of faculty and graduate students")
	]
 	Appr_Supervision_By = models.CharField("*Supervision By", max_length=180, choices=APPR_SUPERVISION_BY)

	#Nature of work
 	APPR_NATURE_OF_WORK = [
		("theoretical", "Nature of work is primarily theoretical, most work on paper/electronic medium"),
		("experimental", "Nature of work is primarily experimental, requiring hands-on work in a lab"),
		("field based", "Nature of work is primarily field based, requiring hands-on work in the field"),
		("computer-related", "Nature of work is primarily computer-related, involving coding/analysis"),
		("combination", "Nature of work is a combination of several types of work")
	]
 	Appr_Nature_Of_Work = models.CharField("*Nature of Work", max_length=180, choices=APPR_NATURE_OF_WORK)
 	
	#Prior Work
	APPR_PRIOR_WORK = [
		("None", "No prior work; student will be starting from basic idea"),
		("Some", "Some prior work; student will build on work of others"),
		("Well-established", "Well-established body of work; student will refine/improved upon efforts of others")
	]
 	Appr_Prior_Work = models.CharField("*Prior Work", max_length=180, choices=APPR_PRIOR_WORK)
	
 	Username = models.CharField(max_length=180)
	
	def __unicode__(self):
		return self.Id

	def __str__(self):
		return self.Id
    
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.Id})

class Student(models.Model):
	First_Name = models.CharField(max_length=80)
	Last_Name = models.CharField(max_length=80)
	CHOICES = (('1','Male'),('2','Female'))
	Gender = models.CharField("*Gender", max_length=25, choices=CHOICES, error_messages={'required':"Please select a Gender type"})
 
	def __unicode__(self):
		return self.First_Name

	def __str__(self):
		return self.First_Name
    
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.First_Name})    
  