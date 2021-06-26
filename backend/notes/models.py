from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    SEMESTER_CHOICES = [
        ('1',"First semester"),
        ('2',"Second semester"),
        ('3', "Third semester"),
        ('4', "Fourth semester"),
        ('5', "Fifth semester"),
        ('6', "Sixth semester"),
        ('7', "Seventh semester"),
        ('8', "Eighth semester"),
    ]
    print(User)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    semester = models.CharField(max_length=50, choices=SEMESTER_CHOICES, default="1")
    subject = models.CharField(max_length=50)
    file = models.FileField(upload_to='notes/%Y/%m/%d/')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Note, self).save(*args, **kwargs)

