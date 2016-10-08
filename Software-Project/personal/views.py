from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

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
	'''
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("title")
		instance.save()
	'''
	# if request.method == "POST":
	# 	print "title" + request.POST.get("content")
	# 	print request.POST.get("title")
	# 	#Post.objects.create(title=title)
	
	return render(request, "personal/index.html", context)
 
def page2(request):
    # Get the result from the session
    return render(request, 'personal/home.html')	
	
	
	
	
    

    

