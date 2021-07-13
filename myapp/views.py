from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
        about = About.objects.first()
        skills = Skills.objects.all()
        education = Education.objects.all()
        exp = Experience.objects.all()
        port = Portfolio.objects.all()
        services = Service.objects.all()
        return render(request,'index.html',{'about':about,'skills':skills,'edu':education,'exp':exp,'port':port,'services':services})