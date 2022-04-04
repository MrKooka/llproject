from django import forms
from .models import CastomUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CastomUser
        fields = ('external_id','name')
        widgets = {'name':forms.TextInput}