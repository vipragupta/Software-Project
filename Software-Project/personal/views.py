from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.template.context_processors import csrf
#from django.core.context_processors import csrf
#from django.views.decorators import csrf

#Import all the forms from form.py
from .forms import ProjectModelForm
from .forms import StudentForm
from .models import ProjectModel
from .models import Student
from .forms import *
from .models import DEPARTMENT as DEP
import copy

#-------------Create your views here-------------------------
def home(request):
	return render(request, "personal/home.html")

#-------------Student views-----------------------------------
def viewprojects(request):
	if not request.user.is_authenticated():
		return render_to_response('personal/login_student.html')
	all_projs = list( ProjectModel.objects.all() )
	context = {}
	details1 = []
 
	for i in all_projs:
		add = []
		add.append(i.Id)
		add.append(i.Appr_Title)
		add.append(i.Appr_Details)
		add.append(i.PF_Department)
		add.append(i.Appr_Special_Requirements)  
		add.append(i.PF_First_Name + "\n" + i.PF_Last_Name)  
		add.append(i.PF_Contact_Number)  
		add.append(i.PF_Email)
		details1.append(add)

	dep_grp = {}
 
	for dep in DEP:
		all_projs = list( ProjectModel.objects.filter(PF_Department = dep[0]) )
		project = []
		for proj in all_projs:
			add = []
			add.append(proj.Id)
			add.append(proj.Appr_Title)
			add.append(proj.Appr_Details)
			add.append(proj.PF_Department)
			add.append(proj.Appr_Special_Requirements)  
			add.append(proj.PF_First_Name + "\n" + i.PF_Last_Name)  
			add.append(proj.PF_Contact_Number)  
			add.append(proj.PF_Email)
			project.append(add)
		if len(project)> 0:   
			dep_grp[dep[1]] = copy.deepcopy(project)

	faculty_grp = {}
	facultyNames = ProjectModel.objects.order_by().values('PF_First_Name', 'PF_Last_Name').distinct()

	for faculty in facultyNames:
		values = faculty.values()     
		name = values[0] + " ".decode("utf-8") + values[1]
		all_projs = list( ProjectModel.objects.filter(PF_First_Name = values[0], PF_Last_Name = values[1]) )
		project = []
		for proj in all_projs:
			
			add = []
			add.append(proj.Id)
			add.append(proj.Appr_Title)
			add.append(proj.Appr_Details)
			add.append(proj.PF_Department)
			add.append(proj.Appr_Special_Requirements)  
			add.append(proj.PF_First_Name + "\n" + i.PF_Last_Name)  
			add.append(proj.PF_Contact_Number)  
			add.append(proj.PF_Email)
			project.append(add)
			   
		if len(project)> 0:   
			faculty_grp[ name ] = copy.deepcopy(project)
		
	context["details1"] = details1
	context["dep_grp"] = dep_grp
	context["faculty_grp"] = faculty_grp
	return render(request, 'personal/viewprojects.html', context)
	
def applyprojects(request):
	if not request.user.is_authenticated():
		return render_to_response('personal/login_student.html')
	studentForm = StudentForm(request.POST or None)

	context = {
		"studentForm": studentForm,
	}
	#print studentForm
	if request.method == "POST":
		if studentForm.is_valid():
			#print studentForm.cleaned_data
			instance = studentForm.save(commit=False)
			instance.save()
			return render(request, 'personal/studenthome.html',context)

	return render(request, 'personal/applyprojects.html',context)	

def facultyhome(request):
    if not request.user.is_authenticated():
		return render_to_response('personal/login_faculty.html')
    return render(request, 'personal/facultyhome.html')

def studenthome(request):
	if not request.user.is_authenticated():
		return render_to_response('personal/login_student.html')
	return render(request, 'personal/studenthome.html')

#----------------Faculty views----------------------------------------
def projects(request):
	if not request.user.is_authenticated():
		return render_to_response('personal/login_student.html')
	username = request.user.username
	all_projs = list( ProjectModel.objects.filter(Username = username) )
	context = {}
	details1 = []
 
	for i in all_projs:
		add = []
		add.append(i.Id)
		add.append(i.Appr_Title)
		add.append(i.Appr_Details)
		add.append(i.Appr_Departments)
		add.append(i.Appr_Special_Requirements)  
		add.append(i.PF_First_Name + "\n" + i.PF_Last_Name)  
		add.append(i.PF_Contact_Number)  
		add.append(i.PF_Email)
		details1.append(add)
	context["details1"] = details1
	return render(request, 'personal/projects.html', context)

def addprojects(request):
    
	if not request.user.is_authenticated():
		return render_to_response('personal/logout.html')

	projectModelForm = ProjectModelForm(request.POST or None)
	context = {
		"projectModelForm": projectModelForm
	}
	
	if request.method == "POST":
		
		if projectModelForm.is_valid():
			#print projectModelForm.cleaned_data
			instance = projectModelForm.save(commit=False)
			if request.user.is_authenticated():
				username = request.user.username
   			instance.Username = username
			instance.save()
			return render(request, 'personal/facultyhome.html',context)

	return render(request, 'personal/addprojects.html',context)	



#Login Authentication related views ---- login_faculty() to logout()
def login_faculty(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('personal/login_faculty.html', c)

def login_student(request):
    c = {}
    c.update(csrf(request))
    '''
    myuserForm = MyuserForm(request.POST or None)
    print csrf(request)
    #print k
    context = {
		"myuserForm": myuserForm
    }

    if request.method == "POST":
        
        print k
        #This is only for database		
        if myuserForm.is_valid():
            instance = myuserForm.save(commit=False)
            #instance.User = csrf(request)
            instance.save()
    '''
    return render(request, 'personal/login_student.html',c)
 
def auth_view_faculty(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return render(request, 'personal/facultyhome.html')	
    else:
        return HttpResponseRedirect('invalid')

def auth_view_student(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return render(request, 'personal/studenthome.html')	
    else:
        return HttpResponseRedirect('invalid')

def loggedin(request):
    return render_to_response('personal/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('personal/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('personal/logout.html')
    