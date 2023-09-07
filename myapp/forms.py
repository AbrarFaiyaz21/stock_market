from django.forms import ModelForm
from django import forms
from .models import SQLData

class SQLDataForm(ModelForm):
    class Meta:
        model = SQLData
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }