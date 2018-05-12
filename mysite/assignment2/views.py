from django.shortcuts import render
from . import models

#login = billy
#password = steelseries

# Create your views here.

def homepage(request):
    return render(request,'homePageblock.html')

def create(request):
    return render(request,'homePageblock.html')

def update(request):
    return render(request,'homePageblock.html')

def delete(request):
    return render(request,'homePageblock.html')

def read(request):
    return render(request,'homePageblock.html')
