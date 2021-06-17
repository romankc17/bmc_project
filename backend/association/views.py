from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
from .forms import EventForm

from datetime import datetime, timedelta
import pytz

tz = pytz.timezone('Asia/Kathmandu')


def events(request, events_type):
    now = tz.localize(datetime.today())
    if events_type == 'past':
        events = Event.objects.filter(
            date__range=[
                now - timedelta(days=1000), now
            ]
        )
    elif events_type == 'upcoming':
        events = Event.objects.filter(
            date__range=[
                now, now + timedelta(days=1000)
            ]
        )
    else:
        return HttpResponse('<h1>Page was not found</h1>')

    contents = {'events':events}

    return render(request, 'association/events.html', contents)


def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EventForm()

    return render(request, 'association/create_event.html', {'form': form})
