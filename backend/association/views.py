from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import Event
from .forms import EventForm
from django.utils import timezone
from datetime import datetime, timedelta
import pytz

tz = pytz.timezone('Asia/Kathmandu')


# render all past events and upcomin events
def events(request, events_type):
    now = tz.localize(datetime.today())
    if events_type == 'past':
        events = Event.objects.filter(
            date__range=[
                now - timedelta(days=1000), now
            ]
        ).order_by('-date')
    elif events_type == 'upcoming':
        events = Event.objects.filter(
            date__range=[
                now, now + timedelta(days=1000)
            ]
        ).order_by('-date')

    elif events_type == 'all':
        events = Event.objects.all().order_by('-date')

    else:
        return HttpResponse('<h1>Page was not found</h1>')

    contents = {'events': events}

    return render(request, 'association/events.html', contents)


def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('events', events_type='all')
    else:
        form = EventForm()
    return render(request, 'association/create_event.html', {'form': form})

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'association/create_event.html'
    success_url = reverse_lazy("events",kwargs={"events_type":"all"})

    def get_initial(self):
        initial_base = super(EventUpdateView,self).get_initial()

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        initial_base['time']=current_time
        return  initial_base

    # def put(self, *args, **kwargs):
