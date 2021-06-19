
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    
    class Meta:
        model = User
        fields = ('emaii', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False) 
        

        batch = self.cleaned_data['batch']
        roll_no = self.cleaned_data['roll_no']

        user.email = self.cleaned_data['email']
        user.username = int(str(batch) + str(roll_no))
        
        if commit:
            user.save()
            
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'batch', 'roll_no','address')