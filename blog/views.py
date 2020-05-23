from django.shortcuts import render, get_object_or_404
from .models import Post

def all_blogs(request):
    posts_count = Post.objects.count
    posts = Post.objects.order_by('-date')[:5]
    template_name = 'blog/all_posts.html'
    context = {}
    # template_name = 'blog/home.html'
    # context = {}
    return render(request, template_name, {'posts':posts, 'posts_count':posts_count})

def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    template_name = 'blog/detail.html'
    return render(request, template_name, {'post':post})
