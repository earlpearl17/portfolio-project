from django.shortcuts import render

from .models import Job
from tutorials.models import Topic

def home(request):
    jobs = Job.objects.all()
    topics = Topic.objects.all()
    context = {
        'jobs': jobs,
        'topics': topics,
    }
    return render(request, 'jobs/home.html', context)

