from django.urls import path, re_path
from . import views

urlpatterns = [
    path('events/e/create/', views.create_event, name='create_event'),
    path('events/', views.events, name='events'),
    path('events/<int:event_id>', views.event_detail, name='event_detail'),
    path("events/<int:pk>/update/", views.EventUpdateView.as_view(), name='update_event'),
    
    path("teams/create/<str:username>/", views.create_team, name="create_team"),
    path("teams/update/<str:username>/",views.update_team,name="update_team"),
    
    path("about/",views.about,name="about"),
]
