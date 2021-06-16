from django.urls import path,include
from . import views

urlpatterns = [
    
    path('register/',views.register, name='user-register' ),
    path('user_login/',views.user_login, name='user-_ogin' ),
    path('staff_login/',views.staff_login, name='staff_login' ),
]