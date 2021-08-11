from django.db import models

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


def get_img_upload_path(instance, filename):
    slug_title=slugify(instance.title)
    if len(slug_title)>25:
        slug_title=slug_title[:15]
    return f'events/{slug_title}/{filename}'

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000,blank=True)
    venue = models.CharField(max_length=50)
    host = models.CharField(max_length=50,null=True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to=get_img_upload_path,default='events/event_default.jpg')

    def __str__(self):
        return self.title


class Team(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    CATEGORY_CHOICES = (
        ("G","General Member"),
        ("B","Board Member"),
        ("A","ADVISOR")
    )
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        default="G"
    )
    position=models.CharField(max_length=25,null=True,blank=True)
    linkdin_url=models.URLField(max_length=100,null=True,blank=True)
    facebook_url=models.URLField(max_length=100,null=True,blank=True)
    instagram_url=models.URLField(max_length=100,null=True,blank=True)
    rank=models.IntegerField(default=20)

    def __str__(self):
        return f"Team-{self.category}-{self.user.username}"
