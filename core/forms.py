from django import forms
from .models import LibraryNote

class LibraryNoteForm(forms.ModelForm):
    class Meta:
        model = LibraryNote
        fields = ['title', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Note title'}),
            'url': forms.URLInput(attrs={'class':'form-control','placeholder':'https://...'}),
        }
