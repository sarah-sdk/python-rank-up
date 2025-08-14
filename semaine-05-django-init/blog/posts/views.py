from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def posts_list(request):
  posts = Post.objects.all()
  print(posts)
  return render(request, 'posts/list.html', {'posts': posts})

def post_create(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/posts/')
    
  else:
    form = PostForm()
  
  return render(request, 'posts/form.html', {'form': form})