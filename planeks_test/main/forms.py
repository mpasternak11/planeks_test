from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Scheme


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=10, label='Login')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=4)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=4)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class AddSchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = '__all__'


class GenerateDataForm(forms.Form):
    num_records = forms.IntegerField(min_value=1, label='Number of records to generate')
