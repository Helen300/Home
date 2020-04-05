from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

def homepage(request):
    #return HttpResponse("Hello World")
    html = render_to_string('templates/home/homepage.html')
    return HttpResponse(html)
