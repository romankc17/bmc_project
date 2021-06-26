from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/%Y/%m/%d/")

    def __str__(self):
        return self.title


class Like(models.Model):
    count = models.IntegerField(default=0, null=True, blank=True)
