from django.shortcuts import render
from django.contrib import messages

from .models import Topic, Tutorial

def tutorials(request, topic_id):
    """Show all Tutorials by topic"""
    topics = Topic.objects.all()
    topic = Topic.objects.get(pk=topic_id)
    tutorials = Tutorial.objects.filter(topic__id=topic_id).order_by('date_added')
    name = topic.text.lower()
    if (' ' in name):
        name = "_".join( name.split() )
    context = {'tutorials': tutorials, 'topics': topics}
    file = name + '.html'
    path = 'tutorials/' + name + '/' + file
    return render(request, path, context)

def topic_tutorial(request, topic_id, tutorial_id):
    """Show specific Tutorial by topic"""
    topics = Topic.objects.all()
    tutorial = Tutorial.objects.get(topic__id=topic_id, id=tutorial_id)
    name = tutorial.topic.text.lower()
    if (' ' in name):
        name = "_".join( name.split() )
    file = str(tutorial_id) + ".html"
    path = 'tutorials/' + name + '/' + file
    context = {
        'tutorial': tutorial, 
        'topics': topics
    }
    messages.warning(request, 'Made it to ps_tut view!')
    return render(request, path, context)
    

def powershell(request):
    """Show all PowerShell Tutorials"""
    tutorials = Tutorial.objects.filter(topic__text='Powershell').order_by('date_added')
    context = {'tutorials': tutorials}
    return render(request, 'tutorials/powershell/powershell.html', context)

def scripting(request):
    """Show all Linux Shell Scripting Tutorials"""
    tutorials = Tutorial.objects.filter(topic__text='Shell Scripting').order_by('date_added')
    context = {'tutorials': tutorials}
    return render(request, 'tutorials/shell_scripting/shell_scripting.html', context)

def network(request):
    """Show all Networking Fundamentals Tutorials"""
    tutorials = Tutorial.objects.filter(topic__text='Networking').order_by('date_added')
    context = {'tutorials': tutorials}
    return render(request, 'tutorials/networking/networking.html', context)

def misc(request):
    """Show all Miscellaneous Tutorials"""
    tutorials = Tutorial.objects.filter(topic__text='Miscellaneous').order_by('date_added')
    context = {'tutorials': tutorials}
    return render(request, 'tutorials/miscellaneous/miscellaneous.html', context)
