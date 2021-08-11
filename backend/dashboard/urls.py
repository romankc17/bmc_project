from django.urls import path
from . import views as dashboard_views

urlpatterns = [
    path('events/', dashboard_views.events, name='dashboard-events'),
    
]
