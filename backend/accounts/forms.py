
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import UserProfile,VerificationImage



class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('email','password1', 'password2')
        
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email, is_active=True).exists():
            raise ValidationError("Email Already exists")
        return self.cleaned_data

SEC_CHOICES = [
    ('','SECTION'),
    ('A','A'),
    ('B','B')
]

class UserProfileForm(forms.ModelForm):
    sec = forms.ChoiceField(choices=SEC_CHOICES)
    
    class Meta:
        model = UserProfile
        fields = ('name','batch', 'roll_no','sec')

class VerificationImageForm(forms.ModelForm):
    class Meta:
        model=VerificationImage
        fields=('image',)
        