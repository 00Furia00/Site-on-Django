from .models import Table
from django.forms import ModelForm, TextInput

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ["title", "country", "year", "nums"]
        widgets = {
            "title": TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'input name'
            }),
            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input country'
            }),
            "year": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input year'
            }),
            "nums": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input nums'
            }),
        }



