from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Blog
from django.contrib.auth.models import User

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

    # adding extra context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet if needed
        # Add here

        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content', 'image']
    template_name = "blog/blog_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    success_url = "/blog"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog
    success_url = "/blog"

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author
