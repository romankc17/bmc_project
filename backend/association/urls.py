from django.urls import path, re_path
from . import views

urlpatterns = [
    path('events/create/', views.create_event, name='create_event'),
    path('events/<str:events_type>/', views.events, name='events'),
    path("events/<int:pk>/update/", views.EventUpdateView.as_view(), name='update_event'),
    path("teams/create/<int:profile_id>/", views.create_team, name="create_team"),
    path("teams/update/<int:team_id>/",views.update_team,name="update_team")
]
