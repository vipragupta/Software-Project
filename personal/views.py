from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'personal/backup.html')


def index2(request):
    return render(request, 'personal/header.html')