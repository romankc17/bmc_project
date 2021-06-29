from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField()
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/%Y/%m/%d/")

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    comment = models.TextField(max_length=1000)
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post({self.blog.id})->Comment({self.id})'

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    liked_at = models.DateField(auto_now_add=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,null=True,related_name='likes')
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,related_name='likes')