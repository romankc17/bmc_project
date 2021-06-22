from django.contrib.auth import authenticate
from django.db import reset_queries
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
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
            messages.success(request,"your username is (your_batch)-(ronn_no)" )
            return redirect('login')

        else:
            return render(request,'accounts/register.html')
           

            
            
            
    else:
        user_form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'user_form':user_form, 'profile_form': profile_form}
    return render(request, 'accounts/register.html',context)

def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']
        print("hello")

        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"username or password not correct")
            
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
        
        
        
def logout(request):
    
    auth.logout(request)
    return redirect('/')

