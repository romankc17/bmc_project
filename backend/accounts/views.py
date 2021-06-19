from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()
    return render (request, 'accounts/register.html',  {'form': form})

