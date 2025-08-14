from django.shortcuts import get_object_or_404, render, redirect
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
      return redirect('posts_list')
    
  else:
    form = PostForm()
  
  return render(request, 'posts/form.html', {'form': form})

def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      return redirect('posts_list')
    
  else:
    form = PostForm(instance=post)
    return render(request, 'posts/form.html', {'form': form})
    
def post_delete(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    post.delete()
    return redirect('posts_list')
  return render(request, 'posts/confirm_delete.html', {'post': post})
    