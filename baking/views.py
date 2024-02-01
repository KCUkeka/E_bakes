from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bakery

# Create your views here.

def welcome (request):
    bakery = Bakery.objects.all()
    return render (request, 'welcome.html', { 'bakery': bakery})

def index (request):
    return render (request, 'index.html')

def about (request):
    return render (request, 'about.html')


# this is for my baseurl and home templates
""" def baseurl (request):
    return render (request, 'baseurl.html')

def home (request):
    return render (request, 'home.html') """


#  getting a main page url
#  def index(request):
#     baseurl = request.build_absolue_uri()
#     return render_to_response('your-template.html'), { 'baseurl' : baseurl } 