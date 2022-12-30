from django import forms
from .models import Libro


class libroform(forms.ModelForm):
    class Meta:
        model= Libro
        fields= '__all__'