from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'posts/post_list.html', {'posts':posts})

def base(request):
    return render(request,'posts/base.css')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_indi.html', {'post': post})


