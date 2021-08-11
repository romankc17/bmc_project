from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin,PermissionRequiredMixin

from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    
)

from .models import Notice


class NoticeListView(ListView):
    model = Notice
    template_name = 'notices/notices.html'
    context_object_name = 'notices'
    ordering = ['-created_at']
    paginate_by = 8
    
class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'notices/notice_detail.html'
    context_object_name = 'notice'
    
class NoticeCreateView(CreateView):
    model = Notice
    template_name = 'notices/notice_form.html'
    fields = ['title','description']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        return self.request.user.is_superuser
    
class NoticeUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Notice
    fields = ['title','description']
    template_name = 'notices/notice_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
        
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    success_url = '/notices'
    template_name = 'notices/notice_confirm_delete.html'

    def test_func(self):
        return self.request.user.is_superuser
