from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

def get_img_upload_path(instance, filename):
    return f'accounts/{instance.user.username}/{filename}'

SEC_CHOICES = [
    ('A','A' ),
    ('B','B')
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    sec = models.CharField(max_length=1,choices=SEC_CHOICES,default="A")
    permanent_address = models.CharField(max_length=200,default=None,blank=True,null=True)
    temporary_address = models.CharField(max_length=200,default=None,blank=True,null=True)
    batch = models.BigIntegerField()
    image= models.ImageField(upload_to=get_img_upload_path,default="accounts/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username