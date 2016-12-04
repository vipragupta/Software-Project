from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
import datetime
from django.core.files.storage import FileSystemStorage
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.

#list of applicable departments
DEPARTMENT = [
	('None','None'),
	('Aerospace', 'Aerospace Engineering'),
	('Applied Mathematics', 'Applied Mathematics'),
	('Architectural', 'Architectural Engineering'),
	('Chemical', 'Chemical Engineering'),
	('Biological', 'Biological Engineering'),
	('Civil', 'Civil Engineering'),
	('Computer Science', 'Computer Science'),
	('Electrical', 'Electrical Engineering'),
	('Electrical and Computer', 'Electrical and Computer Engineering'),
	('Engineering Physics', 'Engineering Physics'),
	('Environmental', 'Environmental Engineering'),
    ('Mechanical', 'Mechanical Engineering'),
    ('Technology Arts and Media', 'Technology Arts and Media'),
]

US_STATES = [('NN', ''),
('AL', 'Alabama'),
 ('AK', 'Alaska'),
 ('AZ', 'Arizona'),
 ('AR', 'Arkansas'),
 ('CA', 'California'),
 ('CO', 'Colorado'),
 ('CT', 'Connecticut'),
 ('DE', 'Delaware'),
 ('DC', 'District of Columbia'),
 ('FL', 'Florida'),
 ('GA', 'Georgia'),
 ('HI', 'Hawaii'),
 ('ID', 'Idaho'),
 ('IL', 'Illinois'),
 ('IN', 'Indiana'),
 ('IA', 'Iowa'),
 ('KS', 'Kansas'),
 ('KY', 'Kentucky'),
 ('LA', 'Louisiana'),
 ('ME', 'Maine'),
 ('MD', 'Maryland'),
 ('MA', 'Massachusetts'),
 ('MI', 'Michigan'),
 ('MN', 'Minnesota'),
 ('MS', 'Mississippi'),
 ('MO', 'Missouri'),
 ('MT', 'Montana'),
 ('NE', 'Nebraska'),
 ('NV', 'Nevada'),
 ('NH', 'New Hampshire'),
 ('NJ', 'New Jersey'),
 ('NM', 'New Mexico'),
 ('NY', 'New York'),
 ('NC', 'North Carolina'),
 ('ND', 'North Dakota'),
 ('OH', 'Ohio'),
 ('OK', 'Oklahoma'),
 ('OR', 'Oregon'),
 ('PA', 'Pennsylvania'),
 ('RI', 'Rhode Island'),
 ('SC', 'South Carolina'),
 ('SD', 'South Dakota'),
 ('TN', 'Tennessee'),
 ('TX', 'Texas'),
 ('UT', 'Utah'),
 ('VT', 'Vermont'),
 ('VA', 'Virginia'),
 ('WA', 'Washington'),
 ('WV', 'West Virginia'),
 ('WI', 'Wisconsin'),
 ('WY', 'Wyoming')]# Create your models here

RACE_CHOICES = [
			 ('None', 'None'),
			 ('AI_AN', 'American Indian or Alaskan Native'),
			 ('B_AA', 'Black or African-American'),
			 ('NH_OPI', 'Native Hawaiian or other Pacific Islander'),
			 ('A', 'Asian'),
			 ('W', 'White'),
			 ('O', 'Other'),
			 ('DN', 'Do Not Wish to Provide'),
			]

LEVEL_IN_SCHOOL=[('F','Freshman'),
				('SO','Sophomore'),
				('J','Junior'),
				('SE','Senior'),
				('FSE','5th Year Senior'),
				]

TRUE_FALSE=[('1','True'),
				('0','False')
				]

TRUE_FALSE_NS=[('1','True'),
				('0','False'),
				('2','Not Sure')
				]

GENDER_CHOICES = [('M','Male'),('F','Female'),('D','Do Not Wish to Provide')]

ROLES = (
    (0, 'Student'),
    (1, 'Faculty'),
    (2, 'Admin'),
    (3, 'CAES Staff'),
)

DEGREE = [
	('BS', 'BS'),
	 ('MS', 'MS'),
	]

# Create your models here

def getProjectList():
	all_projs = list(ProjectModel.objects.all())
	ret = [('0',None)]
	for i in all_projs:
		k = str(i.Id)
		v = str(k).decode("utf-8") + ":".decode("utf-8") + i.Appr_Title
		ret.append( (k,v) )
	return ret


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
	Appr_Special_Requirements = models.CharField("*Special skillset required", max_length=1000)
	#need to split these things, based on comma
	Appr_Departments = MultiSelectField("*Choose one or more departments", max_length=120, choices=DEPARTMENT)
	
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
 	Appr_Prior_Work = models.CharField("*Prior Work on project", max_length=180, choices=APPR_PRIOR_WORK)
	
	Min_GPA = models.FloatField("*GPA (Should be between 0 to 4)", validators = [MinValueValidator(0.0), MaxValueValidator(4.0)])
	Requirement1 = models.CharField("*Requirement I", max_length=100)
	Requirement2 = models.CharField("*Requirement II", max_length=100)
	Requirement3 = models.CharField("*Requirement III", max_length=100) 

 	Username = models.CharField(max_length=180)
	'''
 	Student_Selected = models.IntegerField("Student ID", default=0) #stores the students_id
 	IS_Facutly_Selected = models.IntegerField("IS_Facutly_Selected", default=0) #boolean(0/1) value
 	IS_admin_Selected = models.IntegerField("IS_admin_Selected", default=0) #boolean(0/1) value
	'''
	def __unicode__(self):
		return self.Id

	def __str__(self):
		return self.Id
    
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.Id})

class Student(models.Model):
	
	First_Name = models.CharField("*First Name",max_length=80)
	Last_Name = models.CharField("*Last Name", max_length=80)
	Student_Id = models.IntegerField("*Student ID", primary_key=True)
	Gender = models.CharField("*Gender", max_length=25, choices=GENDER_CHOICES, error_messages={'required':"Please select a Gender type"})
 	Race = models.CharField("*Race", max_length=100, choices=RACE_CHOICES)
 	Address_Line_1 = models.CharField("*Address1", max_length=200)
 	Address_Line_2 = models.CharField("Address2", max_length=200)
 	City = models.CharField("*City", max_length=80)
 	State = models.CharField("*State", max_length=25, choices=US_STATES, error_messages={'required':"Please select a State"})
 	Zip = models.CharField("*Zip", max_length=5)
 	Country = models.CharField("*Country", max_length=80, default="United States")
 	Phone = models.IntegerField("*Phone")
 	Email = models.EmailField("*Email")

 	SAddress_Line_1 = models.CharField("*Summer Address1", max_length=200)
 	SAddress_Line_2 = models.CharField("Summer Address2", max_length=200)
 	SCity = models.CharField("*Summer City", max_length=80)
 	SState = models.CharField("*Summer State", max_length=25, choices=US_STATES, error_messages={'required':"Please select a State"})
 	SZip = models.CharField("*Summer Zip", max_length=5)
 	SCountry = models.CharField("*Summer Country", max_length=80, default="United States")
 	SPhone = models.IntegerField("*Summer Phone", null = True)
 	SEmail = models.EmailField("*Summer Email")
 	Enrollment = models.CharField("", choices=TRUE_FALSE, max_length=60)
 	Primary_Major = models.CharField("*Primary Major", max_length=50, choices=DEPARTMENT)
 	GPA = models.FloatField	("*GPA (Should be between 0 to 4)", validators = [MinValueValidator(0.0), MaxValueValidator(4.0)])
 	Secondary_Major = models.CharField("Secondary Major", max_length=50, choices=DEPARTMENT)
	Degree_Level = models.CharField("What degree are you pursuing?", max_length=50, choices=DEGREE)
	Level = models.CharField("*Level in school as of next fall", max_length=50, choices=LEVEL_IN_SCHOOL)
	Anticipated_Graduation = models.DateField("*Anticipated Graduation Date",default=datetime.datetime.now)
	Previous_Research = models.CharField("Do you have previous research experience?",choices=TRUE_FALSE, max_length=20)
	Availability = models.CharField("", choices=TRUE_FALSE, max_length=60)
	
	PROJECTS = getProjectList()
	
	Applied_Before = models.CharField("*Have you applied for Discovery Learning Apprenticeship before?", choices=TRUE_FALSE, max_length=20)
	Got_DLA_Before = models.CharField("Have you worked for DLA before?", max_length=50, choices=TRUE_FALSE)
	First_Preference = models.CharField("*First Preference", max_length=200, choices=PROJECTS)
	Two_Preference = models.CharField("Two Preference", max_length=200, choices=PROJECTS)
	Three_Preference = models.CharField("Three Preference", max_length=200, choices=PROJECTS)
	Four_Preference = models.CharField("Four Preference", max_length=200, choices=PROJECTS)
	Five_Preference = models.CharField("Five Preference", max_length=200, choices=PROJECTS)
	Background_check = models.CharField(max_length=50, choices=TRUE_FALSE_NS)
	Discrimination_training = models.CharField(max_length=50, choices=TRUE_FALSE_NS)
	SSN= models.IntegerField("*Last four digits of your Social Security Number: (this will only be used to acess your background check information)")
	Skills = models.CharField("Please list the three skills or qualifications that you feel make you a great candidate for the positions you selected. (Could be knowledge of a programming language, knowledge of a field, courses taken, personal characteristics, etc. If appropriate, note your match to requirements in job description. Please note responses are limited to 75 characters.)", max_length=300)
	Skills_1 = models.CharField("1. ", max_length=100)
	Skills_2 = models.CharField("2. ", max_length=100)
	Skills_3 = models.CharField("3. ", max_length=100)
	
	P1_Req1 = models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P1_Req2= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P1_Req3= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	
	P2_Req1= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P2_Req2= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P2_Req3= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	
	P3_Req1= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P3_Req2= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P3_Req3= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	
	P4_Req1= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P4_Req2= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P4_Req3= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)

	P5_Req1= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P5_Req2= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)
	P5_Req3= models.CharField("Title Req1", max_length=50, choices=TRUE_FALSE, default = False)

	Project_selected_for = models.IntegerField("Project ID", default=0) #stores the project_id 
	Upload=models.CharField(max_length=100)
	#Resume = models.FileField("*Resume", storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='Resume', default='settings.MEDIA_ROOT/default/temp.txt')
	#Cover_Letter = models.FileField("*Cover Letter", storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='Cover_Letter', default='settings.MEDIA_ROOT/default/temp.txt')

	def __unicode__(self):
		return self.First_Name

	def __str__(self):
		return self.First_Name
    
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.First_Name})    

class Myuser(models.Model):
	user = models.OneToOneField(User)
	role = models.IntegerField("*Student/Faculties Unique Id")
	uid = models.CharField("*Role", choices=ROLES, max_length=5)