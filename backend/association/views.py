from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from .models import Event, Team
from .forms import EventForm, TeamForm
from django.utils import timezone
from datetime import datetime, timedelta
import pytz

from accounts.models import UserProfile

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
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('events', events_type='all')
        else:
            print(form.errors)
    else:
        form = EventForm()
    return render(request, 'association/create_event.html', {'form': form})


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


def create_team(request, profile_id):
    if request.method == "POST":
        profile = get_object_or_404(UserProfile, id=profile_id)
        form = TeamForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.profile = profile
            obj.save()

            return render(request, 'association/teams.html', teams=Team.objects.all())
    else:
        form = TeamForm()

    return render(request, 'association/create_team.html', {'form': form})


def update_team(request, team_id):
    instance = Team.objects.get(id=team_id)
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
