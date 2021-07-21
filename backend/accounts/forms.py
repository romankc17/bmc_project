
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile,VerificationImage

SEC_CHOICES = [
    ('','SECTION'),
    ('A','A'),
    ('B','B')
]

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = ('email','password1', 'password2')



class UserProfileForm(forms.ModelForm):
    
    sec = forms.ChoiceField(choices=SEC_CHOICES)
    class Meta:
        model = UserProfile
        fields = ('name','batch', 'roll_no','sec')

class VerificationImageForm(forms.ModelForm):
    class Meta:
        model=VerificationImage
        fields=('image',)
        