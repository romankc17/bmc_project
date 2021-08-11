from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.NoticeListView.as_view(), name='notices'),
]