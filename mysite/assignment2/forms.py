from django import forms
from .models import *

class gameEntryForm(forms.ModelForm):
    class Meta:
        model = game
        fields = ('gameName','description','price','releaseDate','publisher','systemRequirements')
