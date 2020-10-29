from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog
from tutorials.models import Topic

def allblogs(request):
    # return objects in descending order
    blogs = Blog.objects.order_by('-pub_date')
    topics = Topic.objects.all().order_by('text')
    context = {'blogs':blogs, 'topics':topics}
    return render(request, 'blog/allblogs.html', context)

#def detail(request, blog_id):
def detail(request, blog_id, slug=None):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    topics = Topic.objects.all()
    context = {'blog':detailblog, 'topics':topics}
    # Redirect with a 301 in case someone uses the ID based url. This ensures
    # that the canonical url is the keyword based one and will attribute
    # backlinks and search rankings to our keyword based url.
    if request.path != detailblog.get_absolute_url():
        return redirect(detailblog, permanent=True)
    return render(request, 'blog/detail.html', context)
