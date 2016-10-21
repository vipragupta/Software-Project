from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import LoginForm
from .forms import PrimaryFacultyForm
from .forms import SecondFacultyForm
from .forms import ApprenticeshipForm


# Create your views here.

def home(request):
	return render(request, "personal/home.html")

def login(request):
	loginform = LoginForm(request.POST or None)
	context = {
		"loginform": loginform
	}
	
	return render(request, 'personal/login.html',context)

def studenthome(request):
    return render(request, 'personal/studenthome.html')	

def facultyhome(request):
    return render(request, 'personal/facultyhome.html')

def projects(request):
    return render(request, 'personal/projects.html')

def addprojects(request):
	primaryfacultyform = PrimaryFacultyForm(request.POST or None)
	secondfacultyform = SecondFacultyForm(request.POST or None)
	apprenticeshipform = ApprenticeshipForm(request.POST or None)
	context = {
		"primaryfacultyform": primaryfacultyform,
		"secondfacultyform": secondfacultyform,
		"apprenticeshipform": apprenticeshipform
	}
	
	if request.method == "POST" and primaryfaculty.is_valid():
		print primaryfaculty.cleaned_data
	return render(request, 'personal/addprojects.html',context)
	
	
	
    

    

