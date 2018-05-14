from django.shortcuts import *
from assignment2.models import *
from assignment2.forms import *
from django.http import *
from django.views.decorators.csrf import *
from django.template import RequestContext

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
    pageData = {'names':game.objects.all()}
    return render(request,'readBlock.html',pageData)

def deleteResult(request):
    game.objects.filter(gameName='').delete()
    return render(request,'readBlock.html')

@csrf_protect
def createGameEntry(request):
    if request.POST:
        form = gameEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = gameEntryForm()
    args={}
    args['form'] = form
    return render(request,'createFormBlock.html',args)
