from django.shortcuts import render, get_object_or_404

from .models import Blog
from tutorials.models import Topic

def allblogs(request):
    blogs = Blog.objects
    topics = Topic.objects.all()
    # return objects in descending order
    #blogs = Blog.objects.order_by('-pub_date')
    #filter(client=client_id).order_by('-check_in')
    context = {'blogs':blogs, 'topics':topics}
    return render(request, 'blog/allblogs.html', context)

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    topics = Topic.objects.all()
    context = {'blog':detailblog, 'topics':topics}
    return render(request, 'blog/detail.html', context)
