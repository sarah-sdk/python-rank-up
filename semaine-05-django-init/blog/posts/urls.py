from django.urls import path
from . import views

urlpatterns = [
  path('', views.posts_list, name='posts_list'),
  path('add/', views.post_create, name='post_create'),
]