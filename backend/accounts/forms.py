
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True,max_length=25)
    last_name = forms.CharField(required=True,max_length=25)

    class Meta:
        model = User
        fields = ('email','first_name','last_name','password1', 'password2')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('batch', 'roll_no','address')