from django.forms import ModelForm
from django import forms
from .models import Event

from django.utils import timezone

from datetime import datetime

import pytz
tz = pytz.timezone('Asia/Kathmandu')

class EventForm(ModelForm):
    date = forms.DateField(input_formats=['%Y-%m-%d'])
    time = forms.TimeField(input_formats=['%H:%M'])

    class Meta:
        model = Event
        fields = ['title', 'description', 'venue', 'host', 'date', 'time','image']

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        event_dt = datetime.combine(date, time)
        now = timezone.localtime()
        if now > tz.localize(event_dt):
            raise forms.ValidationError("Date and time must be set for future !!")

    def save(self):
        data = self.cleaned_data
        event = Event(
            title=data['title'],
            description=data['description'],
            venue=data['venue'],
            host=data['host'],
            image=data['image'],
            date=datetime.combine(data['date'],data['time'])
        )
        event.save()




    # def clean_title(self):
    #     title =  self.cleaned_data['title']
    #     if 'event' not in title:
    #         raise forms.ValidationError("invalid title")
