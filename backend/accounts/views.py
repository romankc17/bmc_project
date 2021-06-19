from django.db import reset_queries
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import ExtendedUserCreationForm, UserProfileForm

# Create your views here.
def register(request):
    if request.method == 'POST':

        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        
        if form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            return redirect('index')
            
            
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form':form, 'profile_form': profile_form}
    return render(request, 'accounts/register.html')


    return render (request, 'accounts/register.html',  {'form': form})

