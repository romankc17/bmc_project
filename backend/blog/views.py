from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .models import Blog, Comment
from django.contrib.auth.models import User

import datetime

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blogs.html"
    context_object_name = "blogs"
    paginate_by = 5

    # adding extra context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet if needed

        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        context['comment_form']=form
        print(context)
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content', 'image']
    template_name = "blog/blog_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content', 'image']
    success_url = "/blogs"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = "/blogs"

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author
    
@login_required
def create_comment(request,blog_slug):
    if request.method == 'POST':
        blog = Blog.objects.get(slug = blog_slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user=request.user
            comment.commented_at = datetime.datetime.now()
            comment.save()

        return redirect("blog_detail",slug=blog_slug)

    else:
        return Http404("Invalid Operation")

