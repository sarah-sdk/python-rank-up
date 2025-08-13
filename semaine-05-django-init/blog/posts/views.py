from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
  posts = Post.objects.all()
  print(posts)
  return render(request, 'posts/list.html', {'posts': posts})