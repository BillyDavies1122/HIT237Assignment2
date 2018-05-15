"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from assignment2 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',views.homepage,name='home'),
    #URLS relating to the creation of new data
    url(r'^create/$',views.create,name='create'),
    url(r'^createGame/$',views.createNewEntry,name='createGame'),
    url(r'^createPublisher/$',views.createNewEntry,name='createPublisher'),
    url(r'^createSystReq/$',views.createNewEntry,name='createSystReq'),

    #URLS relating to displaying he current data
    url(r'^read/$',views.read,name='read'),
    url(r'^readGame/$',views.readEntries,name='readGame'),
    url(r'^readPublisher/$',views.readEntries,name='readPublisher'),
    url(r'^readSystReq/$',views.readEntries,name='readSystReq'),

    url(r'^update/$',views.update,name='update'),

    #URLS relating to deleting the current data
    url(r'^delete/$',views.delete,name='delete'),
    url(r'^deleteGame/$',views.deleteEntry,name='deleteGame'),
    url(r'^deletePublisher/$',views.deleteEntry,name='deletePublisher'),
    url(r'^deleteSystReq/$',views.deleteEntry,name='deleteSystReq'),
]
