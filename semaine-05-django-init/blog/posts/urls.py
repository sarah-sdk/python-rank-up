from django.urls import path
from . import views

urlpatterns = [
  path('', views.posts_list, name='posts_list'),
  path('add/', views.post_create, name='post_create'),
  path('<pk>/edit/', views.post_edit, name='post_edit'),
  path('<pk>/delete/', views.post_delete, name='post_delete'),
]