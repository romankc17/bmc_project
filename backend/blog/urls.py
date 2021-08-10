from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(),name='blogs'),
    path('b/<str:slug>/', views.BlogDetailView.as_view(),name='blog_detail'),
    path('b/<str:slug>/update/', views.BlogUpdateView.as_view(),name='blog_update'),
    path('b/<str:slug>/delete/', views.BlogDeleteView.as_view(),name='blog_delete'),
    path('create/', views.BlogCreateView.as_view(),name='blog_create'),
    
]