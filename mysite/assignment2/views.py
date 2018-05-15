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
def update(request):
    return render(request,'homePageblock.html')
def delete(request):
    return render(request,'deleteChoiceBlock.html')

def deleteEntry(request):
    if 1==0:
        pass
    else:
        if request.path == '/deleteGame/':
            return render(request,'delete.html')
        elif request.path == '/deletePublisher/':
            return render(request,'delete.html')
        elif request.path == '/deleteSystReq/':
            return render(request,'delete.html')




def read(request):
    return render(request,'readChoiceBlock.html')

def readEntries(request):
    if request.path == '/readGame/':
        pageData = {'names':game.objects.all()}
        return render(request,'readBlock.html',pageData)
    elif request.path == '/readPublisher/':
        pageData = {'names':publisher.objects.all()}
        return render(request,'readBlock.html',pageData)
    elif request.path == '/readSystReq/':
        pageData = {'names':systemRequirements.objects.all()}
        return render(request,'readBlock.html',pageData)


def create(request):
    return render(request,'createChoiceBlock.html')

@csrf_protect
def createNewEntry(request):
    if request.POST:
        if request.path == '/createGame/':
            form = gameEntryForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'homePageblock.html')
        if request.path == '/createPublisher/':
            form = publisherEntryForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'homePageblock.html')
        if request.path == '/createSystReq/':
            form = systemRequirementsEntryForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'homePageblock.html')
    else:
        if request.path == '/createGame/':
            form = gameEntryForm()
        elif request.path == '/createPublisher/':
            form = publisherEntryForm()
        elif request.path == '/createSystReq/':
            form = systemRequirementsEntryForm()
    formContainer = {}
    formContainer['form'] = form
    return render(request,'createFormBlock.html',formContainer)
