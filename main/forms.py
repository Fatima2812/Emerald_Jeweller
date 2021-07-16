from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class edituserprofile(UserChangeForm):
    password= None
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels= {'email': 'Email'}

class SubscribeForm(forms.Form):
    email = forms.EmailField()