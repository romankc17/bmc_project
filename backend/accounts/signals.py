from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def send_mail(sender,instance,**kwargs):
    print("Signal triggered")
    instance.email_user("Welcome to the site","Thank you for signing up")
    
   

