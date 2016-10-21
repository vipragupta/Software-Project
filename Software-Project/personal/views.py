from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
#from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.context_processors import csrf

from .forms import PostForm
from .models import Post
# Create your views here.


def index(request):
	form = PostForm(request.POST or None)
	context = {
		"form": form,
	}
	print form
	print "hi\n"
	return render(request, "personal/index.html", context)

#login
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
    