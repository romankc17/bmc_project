from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


from .models import Team,Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','venue','host','date')
    ordering = ('-date',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','username','position','linkdin_url','facebook_url','instagram_url','rank')
    
    def name(self,obj):
        return obj.user.userprofile.name
    
    def username(self,obj):
        url =  url = (
            reverse("admin:accounts_userprofile_change", kwargs={'object_id': obj.user.userprofile.id})
            + "?"
            + urlencode({"team_id": obj.id})
        )
        return format_html(f"<a href='{url}'>{obj.user.username}</a>")
    
    