from django.contrib import messages
from django.shortcuts import render

from association.models import Event
from notices.models import Notice


def home(request):
    events = Event.objects.order_by('-date')[:2]
    context = {
        'events': events,
        'notices':Notice.objects.order_by('-created_at')[:2]
    }   
    return render(request, 'index.html', context)