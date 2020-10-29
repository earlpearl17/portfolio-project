from django.shortcuts import render

from .models import Job
from tutorials.models import Topic

def dev(request):
    jobs = Job.objects.all().order_by('type')
    # objects = Model.objects.values('var1', 'var2', 'var4')
    objects = Job.objects.values('title','type','url','image','summary')
    # types = Job.objects.values('type').distinct()
    types = Job.objects.values_list('type', flat=True).distinct()
    # types = {}
    # for t in type:
    #     # Job.objects.filter(type=t)
    #     types[t] = jobs.filter(type=t)
    #topics = Topic.objects.all()
    topics = Topic.objects.all().order_by('id')
    context = {'jobs': jobs,'topics': topics, 'types': types}
    for type in types:
        context[type.lower()] = Job.objects.filter(type=type)
    
    return render(request, 'jobs/home.html', context)

