from django.contrib import admin

from .models import Team,Event

admin.site.register([Team,Event])
