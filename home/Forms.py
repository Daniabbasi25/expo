
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil, Links
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms.models import inlineformset_factory
class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ColorInput(forms.TextInput):
    input_type = 'color'

class CreateProfileForm(forms.ModelForm):
    number=PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='GB')
    )
    class Meta:
        model = Profil
        exclude = ['user', 'slug']
        fields = '__all__'
        # widgets = {
        #     'color': ColorInput()
        # }





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
        fields = "__all__"
        exclude = ('user',)

