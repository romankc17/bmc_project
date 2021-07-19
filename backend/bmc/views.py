from django.contrib import messages
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')