from django import forms
from .models import basketmodel

class BasketForm(forms.ModelForm):
    class Meta:
        model = basketmodel
        fields = ['full_name', 'phone_number', 'card_number', 'book', 'status']
