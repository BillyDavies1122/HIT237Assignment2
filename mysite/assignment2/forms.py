from django import forms
from .models import *

class gameEntryForm(forms.ModelForm):
    class Meta:
        model = game
        fields = ('gameName','description','price','releaseDate','publisher','systemRequirements')
class gameUpdateForm(forms.ModelForm):
    class Meta:
        model = game
        fields = ('gameName','description','price','releaseDate')

class publisherEntryForm(forms.ModelForm):
    class Meta:
        model = publisher
        fields = ('publisherName','Location','dateFounded')
class systemRequirementsEntryForm(forms.ModelForm):
    class Meta:
        model = systemRequirements
        fields = ('memoryNeeded','miniumumDiskSpace','gpuRequired')
