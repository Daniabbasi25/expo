from dataclasses import field, fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil, Links


class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profil
        exclude = ['user', 'color', 'slug']
        fields = '__all__'



class ChangeUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(ChangeUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username']:
            self.fields[fieldname].help_text = None


class UpdateLinksForm(ModelForm):
    class Meta:
        model = Links
        fields = ("link",)

