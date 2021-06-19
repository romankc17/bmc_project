from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000,blank=True)
    venue = models.CharField(max_length=50)
    host = models.CharField(max_length=50,null=True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='events/',default="media/events/event_default.jpg")

    def __str__(self):
        return self.title

