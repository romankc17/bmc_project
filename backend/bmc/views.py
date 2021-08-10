from django.contrib import messages
from django.shortcuts import render

from association.models import Event


def home(request):
    events = Event.objects.order_by('-date')[:2]
    context = {
        'events': events,
    }   
    return render(request, 'index.html', context)