from django.contrib.auth import authenticate
from django.db import reset_queries
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import ExtendedUserCreationForm, UserProfileForm
import nepali_datetime


# Create your views here.
def register(request):
    if request.method == 'POST':

        user_form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        print(dir(profile_form))
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)

            profile = profile_form.save(commit=False)
            
            roll_no = profile_form.cleaned_data['roll_no']
            if len(str(roll_no).strip())==1:
                roll_no = int('0'+str(roll_no).strip())
            user.username = f'{profile.batch}-{profile.roll_no}'

            user.save()
            profile.user = user
            profile.save()
            messages.success(request, f"YOUR USERNAME IS '{user.username}'")
            return redirect('login')
        else:
            print(user_form.errors)
            print(profile_form.errors)

    else:
        user_form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
        
    nepali_current_year = nepali_datetime.datetime.now().year
    context = {'user_form': user_form, 
               'profile_form': profile_form,
               'nepali_current_year':nepali_current_year}
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(user)
            return redirect("/")
        else:
            messages.error(request, "username or password not correct")

            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

