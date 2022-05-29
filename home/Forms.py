from dataclasses import field, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil, Links
from django import forms

class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ColorInput(forms.TextInput):
    input_type = 'color'

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profil
        exclude = ['user', 'slug']
        fields = '__all__'
        widgets = {
            'color': ColorInput()
        }





class ChangeUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(ChangeUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username']:
            self.fields[fieldname].help_text = None


class UpdateLinksForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ("link",)

