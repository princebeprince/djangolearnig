from django.shortcuts import render
from .models import Projects
from django.http import HttpResponse
# Create your views here.


def home(request):
    data = Projects.objects.all()
    return render(request , 'portfolio/home.html',{"projects" :data})