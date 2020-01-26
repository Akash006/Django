from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblog.html', {'blogs':blogs})

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog':detail_blog})