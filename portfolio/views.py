from django.shortcuts import render, redirect
from django.contrib import messages

from tutorials.models import Topic

def home(request):
    topics = Topic.objects.all().order_by('text')
    context = {
        'topics': topics,
    }
    return render(request, 'home.html', context)
    #return render(request, 'portfolio/home.html', context)

#def handler404(request, exception=None):
def handler404(request, exception):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    messages.error(request, 'That resource is not available.')
    return redirect('/') # or redirect('name-of-index-url')
    # OR
    # context = {'message': "That resource is not available."}
    # return render(request, 'jobs/home.html', context)

def handler500(request):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    messages.error(request, 'That server resource is not available.')
    return redirect('/') # or redirect('name-of-index-url')
    # OR
    # context = {'message': "That resource is not available."}
    # return render(request, 'jobs/home.html', context)    