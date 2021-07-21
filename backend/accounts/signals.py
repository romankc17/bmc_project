from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import UserProfile


@receiver(post_save, sender=UserProfile)
def send_mail(sender,instance,created,**kwargs):
    print("Signal triggered")
    
    
    
    
   

