from django.shortcuts import render
from assignment2.models import *

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


def allResults(request):
    results = game.objects.get(gameName='wow')
    pageData = {'names':results}


    return render(request,'readBlock.html',pageData)
