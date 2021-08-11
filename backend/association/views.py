from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from django.contrib.auth.models import User

from .models import Event, Team
from .forms import EventForm, TeamForm
from django.utils import timezone
from datetime import datetime, timedelta
import pytz

from accounts.models import UserProfile

tz = pytz.timezone('Asia/Kathmandu')


# render all past events and upcomin events
def events(request):
    now = tz.localize(datetime.today())
    
    past_events = Event.objects.filter(
        date__range=[
            now - timedelta(days=1000), now
        ]
    ).order_by('-date')
        
    
    upcoming_events = Event.objects.filter(
        date__range=[
            now, now + timedelta(days=1000)
        ]
    ).order_by('-date')

    contents = {
        'past_events': past_events,
        'upcoming_events': upcoming_events,
    }

    return render(request, 'event/events.html', contents)


def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('events', events_type='all')
        else:
            print(form.errors)
    else:
        form = EventForm()
    return render(request, 'association/create_event.html', {'form': form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    latest_events = Event.objects.order_by('-date')[:5]    
    
    context = {
        'event': event,
        'latest_events': latest_events,
    }
    print(timezone.now())
    if event.date > timezone.now():
        print(True)
        context['is_upcoming'] = True
    else:
        print('Fas')
        context['is_upcoming'] = False
        
    return render(request, 'event/event_detail.html',context)

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'association/create_event.html'
    success_url = reverse_lazy("events", kwargs={"events_type": "all"})

    def get_initial(self):
        initial_base = super(EventUpdateView, self).get_initial()

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        initial_base['time'] = current_time
        return initial_base

    # def put(self, *args, **kwargs):


def create_team(request, username):
    if request.method == "POST":
        user = get_object_or_404(User, username=username)
        form = TeamForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = user
            obj.save()

            return render(request, 'association/teams.html', teams=Team.objects.all())
    else:
        form = TeamForm()

    return render(request, 'association/create_team.html', {'form': form})


def update_team(request, username):
    instance = Team.objects.get(id=username)
    if request.method == 'GET':
        form = TeamForm(instance=instance)
    else:
        form = TeamForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            instance.category=data['category']
            instance.position=data['position']
            instance.facebook_url=data['facebook_url']
            instance.linkdin_url=data['linkdin_url']

            return render(request,
                          'association/create_team.html',
                          {'form':form}
             )

    template_name="association/create_team.html"
    context={'form':form}

    return render(request, template_name, context)

def about(request):
    context = {
        'president':Team.objects.filter(position='President')[0],
        'members' : Team.objects.exclude(position="President").order_by('rank')
    }
        
    return render(request, 'about/about.html', context)
