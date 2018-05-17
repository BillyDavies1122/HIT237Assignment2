from django.shortcuts import *
from assignment2.models import *
from assignment2.forms import *
from django.http import *
from django.views.decorators.csrf import *
from django.template import RequestContext
#password for admin app
#login = billy
#password = steelseries

# Create your views here.
def homepage(request):
    return render(request,'homePageblock.html')

def update(request):
    return render(request,'updateChoiceblock.html')

"""
The function below is used to update an object belonging to one of three models.
if the request is a POST it then checks the file path of the request to discover which kind of object is is updating
Then updates the object with the appropriate new information

If the request isnt a POST it checks the file path and uses that to create the correc form type
then returns the form to be rendered.
When that form is submitted the POST part of the function will be used.


"""

def updateEntry(request):
    if request.POST:
        #for game type
        if request.path == '/updateGame/':
            toUpdate = request.POST.get("toUpdate")
            game.objects.filter(gameName = toUpdate).update(
                gameName = request.POST.get("gameName"),
                description= request.POST.get("description"),
                price= request.POST.get("price"),
                releaseDate= request.POST.get("releaseDate"))
            return render(request,'homePageblock.html')
            #for publisher type
        elif request.path == '/updatePublisher/':
            toUpdate = request.POST.get("toUpdate")
            publisher.objects.filter(publisherName = toUpdate).update(
                publisherName = request.POST.get("publisherName"),
                Location = request.POST.get("Location"),
                dateFounded= request.POST.get("dateFounded"))
            return render(request,'homePageblock.html')
            #for system requirements type
        elif request.path == '/updateSystReq/':
            toUpdate = request.POST.get("toUpdate")
            systemRequirements.objects.filter(memoryNeeded = toUpdate).update(
                memoryNeeded= request.POST.get("memoryNeeded"),
                miniumumDiskSpace= request.POST.get("miniumumDiskSpace"),
                gpuRequired= request.POST.get("gpuRequired"))
            return render(request,'homePageblock.html')
    else:
        #for game type
        if request.path == '/updateGame/':
            form = gameUpdateForm()
            #for publisher type
        elif request.path == '/updatePublisher/':
            form = publisherEntryForm()
            #for system requirements type
        elif request.path == '/updateSystReq/':
            form = systemRequirementsEntryForm()
        formContainer = {}
        formContainer['form'] = form
        return render(request,'updateFormblock.html',formContainer)

def delete(request):
    return render(request,'deleteChoiceBlock.html')

'''
Checks if the request is a post, if not it returns the delete.html page where users can specify which entry they want to delete
Gets called again on form submission. Which checks the file path it came from so it knows which model to delete from
Then for the publisher and systemRequirements models it makes sure that there isnt a game using them as a key
If there was it would also delete the game.
'''
def deleteEntry(request):
    if request.POST:
        #Deletes from the game model
        if request.path == '/deleteGame/':
            toDelete = request.POST.get("deletionInput")
            game.objects.filter(gameName=toDelete).delete()
            return render(request,'homePageblock.html')
        #Deletes from the publisher model
        elif request.path == '/deletePublisher/':
            toDelete = request.POST.get("deletionInput")
            checkGameExist = game.objects.filter(publisher__publisherName = toDelete)
            if checkGameExist.count() >= 1:
                return render(request,'homePageblock.html')
            else:
                publisher.objects.filter(publisherName=toDelete).delete()
            return render(request,'homePageblock.html')
        #Deletes from the systemRequirements model
        elif request.path == '/deleteSystReq/':
            toDelete = request.POST.get("deletionInput")
            checkGameExist = game.objects.filter(systemRequirements__memoryNeeded = toDelete)
            if checkGameExist.count() >= 1:
                return render(request,'homePageblock.html')
            else:
                systemRequirements.objects.filter(memoryNeeded=toDelete).delete()
            return render(request,'homePageblock.html')
    else:
        #If game
        if request.path == '/deleteGame/':
            return render(request,'delete.html')
        #if publisher
        elif request.path == '/deletePublisher/':
            return render(request,'delete.html')
        #if system requirements
        elif request.path == '/deleteSystReq/':
            return render(request,'delete.html')
        return render(request,'delete.html')





def read(request):
    return render(request,'readChoiceBlock.html')


'''
The function below reads all the entries in a given model
It checks the file path to find out which model to read
Creates a dict object containing any objects belonging to that model
then returns them to be rendered.

'''
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

'''
The createNewEntry function takes a request and if its a POST action it checks the form data and then sends it to the Database
If its not a POST action it creates the correct form type and then sends it back to the request and renders it.
When that form is submitted the POST part of the function will be ran through


if request is a POST
    form = required form type containing the request data
    if form is valid
    save the forms
    return user to home page
else
    form = correct form type
    formContainer = ['form'] = form
    return the form to the form block page with formcontainer

'''

@csrf_protect
def createNewEntry(request):
    if request.POST:
        #For game type
        if request.path == '/createGame/':
            form = gameEntryForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'homePageblock.html')
        #for publisher type
        elif request.path == '/createPublisher/':
            form = publisherEntryForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'homePageblock.html')
        #for system requirements type
        elif request.path == '/createSystReq/':
            form = systemRequirementsEntryForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'homePageblock.html')
    else:
        #for game type
        if request.path == '/createGame/':
            form = gameEntryForm()
        #for publisher type
        elif request.path == '/createPublisher/':
            form = publisherEntryForm()
        #for system requirements type
        elif request.path == '/createSystReq/':
            form = systemRequirementsEntryForm()
    formContainer = {}
    formContainer['form'] = form
    return render(request,'createFormBlock.html',formContainer)
