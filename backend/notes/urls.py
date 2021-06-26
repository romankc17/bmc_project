from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.note_view_list, name="notes_list"),
                  path('create/', views.note_create_view, name="crate_note"),
                  path('update/<int:id>/', views.note_update_view, name="update_note"),
                  path('delete/<int:id>/', views.note_delete_view, name="delete_note"),

              ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

