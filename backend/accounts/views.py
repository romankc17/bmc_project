from django.db import reset_queries
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import ExtendedUserCreationForm, UserProfileForm

# Create your views here.
def register(request):
    if request.method == 'POST':

        user_form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)

            profile = profile_form.save(commit=False)
            user.username = f'{profile.batch}-{profile.roll_no}'
            user.save()
            profile.user = user
            profile.save()
            return redirect('index')
            
            
    else:
        user_form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'user_form':user_form, 'profile_form': profile_form}
    return render(request, 'accounts/register.html',context)

