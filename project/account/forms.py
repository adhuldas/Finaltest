from projectapp.models import product
from django import forms


class Forms(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'desc', 'img']
