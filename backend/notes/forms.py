from django import forms
from .models import Note
from django.forms import ModelForm


#Model form for Notes
class NoteModelForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            "semester",
            "subject",
            "description",
            'file'
        ]