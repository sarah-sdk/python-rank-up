from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def posts_list(request):
  posts = Post.objects.all()
  print(posts)
  return HttpResponse(', '.join([p.title for p in posts]))
  # return render(request, 'posts/list.html', {'posts': posts})