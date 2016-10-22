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
from .forms import PrimaryFacultyForm
from .forms import SecondFacultyForm
from .forms import ApprenticeshipForm
from .models import Apprenticeship

# Create your views here
def home(request):
	return render(request, "personal/home.html")

def studenthome(request):
    return render(request, 'personal/studenthome.html')	

def facultyhome(request):
    if request.user.is_authenticated():
        username = request.user.username
        Projects = Apprenticeship.objects.filter(PrimaryFaculty = username)
        print Projects
    return render(request, 'personal/facultyhome.html')

def projects(request):
    return render(request, 'personal/projects.html')

def addprojects(request):
	primaryfacultyform = PrimaryFacultyForm(request.POST or None)
	#secondfacultyform = SecondFacultyForm(request.POST or None)
	apprenticeshipform = ApprenticeshipForm(request.POST or None)
	context = {
		"primaryfacultyform": primaryfacultyform,
	#	"secondfacultyform": secondfacultyform,
		"apprenticeshipform": apprenticeshipform
	}
	
	if request.method == "POST":
		if primaryfacultyform.is_valid() and apprenticeshipform.is_valid():
			print primaryfacultyform.cleaned_data
			instance = primaryfacultyform.save(commit=False)
			instanceAppr = apprenticeshipform.save(commit=False)
			instanceAppr.SetPrimaryFaculty(primaryfacultyform.cleaned_data["Email"])			
			instance.save()
			#apprenticeshipform.SecondaryFaculty = ""
			instanceAppr.SetSecondaryFaculty("")
			'''   
			if secondfacultyform.is_valid():
				print secondfacultyform.cleaned_data
				#apprenticeshipform.SecondaryFaculty = secondfacultyform.cleaned_data["Email"]
				instanceAppr.SetSecondaryFaculty(secondfacultyform.cleaned_data["Email"])
				instance2 = secondfacultyform.save(commit=False)
				instance2.save()
			'''	
			print apprenticeshipform.cleaned_data
			instanceAppr.save()

	return render(request, 'personal/addprojects.html',context)	
	
#-------------------------Create additional views above this line---------------------------------------------

#Login Authentication related views ---- login_faculty() to logout()
def login_faculty(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('personal/login_faculty.html', c)

def login_student(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('personal/login_student.html', c)
 
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
    