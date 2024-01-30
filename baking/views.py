from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome (request):
    return render (request, 'welcome.html')

def index (request):
    return render (request, 'index.html')



# this is for my baseurl and home templates
""" def baseurl (request):
    return render (request, 'baseurl.html')

def home (request):
    return render (request, 'home.html') """


#  getting a main page url
#  def index(request):
#     baseurl = request.build_absolue_uri()
#     return render_to_response('your-template.html'), { 'baseurl' : baseurl } 