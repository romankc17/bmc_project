from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=200)
    batch = models.BigIntegerField()
    image= models.ImageField(upload_to='pics')
    
    def __str__(self):
        return self.user.username