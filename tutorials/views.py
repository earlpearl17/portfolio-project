from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Topic, Tutorial

def alltopics(request):
    topics = Topic.objects.all().order_by('id')
    path = 'tutorials/alltopics.html'
    context = {'topics': topics}
    #messages.warning(request, 'Made it to alltopics view!')
    return render(request, path, context)
    #return render(request, 'tutorials/alltopics.html', context)

def tutorials(request, topic_id):
    """Show all Tutorials by topic"""
    topics = Topic.objects.all().order_by('id')
    topic = Topic.objects.get(pk=topic_id)
    tutorials = Tutorial.objects.filter(topic__id=topic_id).order_by('type')
    # tutorials = Tutorial.objects.filter(topic__id=topic_id).order_by('date_added')
    types = Tutorial.objects.filter(topic__id=topic_id).values_list('type', flat=True).distinct()
    #types = Tutorial.objects.values_list('type', flat=True).distinct()

    name = topic.text.lower()
    if (' ' in name):
        name = "_".join( name.split() )

    file = name + '.html'
    path = 'tutorials/' + file
    #context = {'tutorials': tutorials, 'topics': topics, 'file': file}
    context = {'topics': topics, 'file': file, 'types': types}
    for type in types:
        #context[type.lower()] = Tutorial.objects.filter(topic__id=topic_id, type=type)
        context[type.lower()] = Tutorial.objects.filter(topic__id=topic_id, type=type).order_by('id')
    return render(request, path, context)

def topic_tutorial(request, topic_id, tutorial_id, lang, slug=None):
    topics = Topic.objects.all().order_by('id')
    # topics = Topic.objects.all().order_by('text')
    topic = Topic.objects.get(id=topic_id)
    tutorial = Tutorial.objects.get(topic__id=topic_id, id=tutorial_id)
    
    if request.path != tutorial.get_absolute_url():
        return redirect(tutorial, permanent=True)
    # renaming topic to avoid spaces
    name = tutorial.topic.text.lower()
    if (' ' in name):
        name = "_".join( name.split() )
    
    # renaming tutorial to avoid spaces
    tut_name = tutorial.text.lower()
    if (' ' in tut_name):
        tut_name = "_".join( tut_name.split() )
    
    # lang always empty
    if (lang == 'fr'):
        file = name + "-" + tut_name + "_fr.html"
    else:    
        file = name + "-" + tut_name + ".html"
    
    # messages.warning(request, 'Made it to ps_tut view!')
    # messages.warning(request, 'Language: ' + str(lang))    

    path = 'tutorials/' + file
    #context = {'tutorial': tutorial,'topics': topics,'file':file}
    context = {'tutorial': tutorial,'topics': topics,'topic':topic,'file':file}
    return render(request, path, context)

