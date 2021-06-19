from django.urls import path, re_path
from . import views

urlpatterns = [
    path('create_event/', views.create_event, name='create_event'),
    path('events/<str:events_type>/', views.events, name='events'),
    path("events/<int:pk>/update/",views.EventUpdateView.as_view(),name='update_event')
]