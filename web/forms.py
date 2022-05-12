from django import forms
from .models import Customer

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('chat_id','name')
        widgets = {'name':forms.TextInput}