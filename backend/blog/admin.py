from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from .models import Blog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name','username','created_at', 'view_comments_link')
    list_filter = ('author',)
    
    class Meta:
        ordering = ('-created_at',)
    
    def author_name(self, obj):
        return obj.author.userprofile.name
    
    def username(self, obj):
        return obj.author.username
        
    def view_comments_link(self, obj):
        count = obj.comments.count()
        url = (
            reverse("admin:blog_comment_changelist")
            + "?"
            + urlencode({"blog_id": obj.id})
        )
        
        return format_html(f"<a href='{url}'>{count}</a>")
    
    view_comments_link.short_description = "Comments"
    author_name.short_description = "Author"
    
    def has_change_permission(self, request, obj=None):
        return obj is None or obj.author == request.user
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['author', 'slug']
        return self.readonly_fields
    
    def has_add_permission(self, request):
        return False
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','commented_by','commented_at','blog_link')
    list_filter = ('blog','user')
    
    def commented_by(self, obj):
        return obj.user.userprofile.name
    
    def blog_link(self, obj):
        url = (
            reverse("admin:blog_blog_changelist")
            + "?"
            + urlencode({"comment_id": obj.id})
        )
        
        return format_html(f"<a href='{url}'>{obj.blog}</a>")
        
    def has_change_permission(self, request, obj=None):
        return obj is None or obj.user == request.user
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user','commented_at']
        return self.readonly_fields
    
    def has_add_permission(self, request):
        return False