from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    # return objects in descending order
    #blogs = Blog.objects.order_by('-pub_date')
    #filter(client=client_id).order_by('-check_in')
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
