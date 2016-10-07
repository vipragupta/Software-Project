from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

def index (request):
    return render_to_response('/Users/nachiketbhagwat/ebdjango/webapp/sample.html')