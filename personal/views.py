from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

def index(request):
    return render(request, 'personal/backup.html')


def index2(request):
    return render(request, 'personal/header.html')

def post_create(request):
    form = PostForm(request.POST or None)
    print form
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
    # if request.method == "POST":
    # 	print "title" + request.POST.get("content")
    # 	print request.POST.get("title")
    # 	#Post.objects.create(title=title)
    context = {
        "form": form,
    }
    return render(request, "personal/post_form.html", context)

def post_response2(request):
    #print "\nreached here\n\n"
    return HttpResponse("<h1>Thanks for visiting.</h1>")