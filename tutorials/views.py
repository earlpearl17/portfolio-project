from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Topic, Tutorial

def tutorials(request, topic_id):
    """Show all Tutorials by topic"""
    #topics = Topic.objects.all()
    topics = Topic.objects.all().order_by('text')
    topic = Topic.objects.get(pk=topic_id)
    tutorials = Tutorial.objects.filter(topic__id=topic_id).order_by('date_added')
    
    name = topic.text.lower()
    if (' ' in name):
        name = "_".join( name.split() )

    file = name + '.html'
    path = 'tutorials/' + file
    #path = 'tutorials/' + name + '/' + file
    context = {'tutorials': tutorials, 'topics': topics, 'file': file}
    #context = {'tutorials': tutorials, 'topics': topics, 'topic': topic, 'file': file}
    #context = {'tutorials': tutorials, 'topics': topics}
    return render(request, path, context)

def topic_tutorial(request, topic_id, tutorial_id, lang, slug=None):
#def topic_tutorial(request, topic_id, tutorial_id, slug=None):
    """Show specific Tutorial by topic"""
    # NOTE: nothings is returned 
    #if (request.GET.get('lang')):
    #lang = request.GET.get('lang')
    
    topics = Topic.objects.all().order_by('text')
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

# def topic_tutorial_fr(request, topic_id, tutorial_id, lang=lang):
#     """Show specific Tutorial by topic"""
#     topics = Topic.objects.all()
#     tutorial = Tutorial.objects.get(topic__id=topic_id, id=tutorial_id)
    
#     if request.path != tutorial.get_absolute_url():
#         return redirect(tutorial, permanent=True)

#     name = tutorial.topic.text.lower()
#     if (' ' in name):
#         name = "_".join( name.split() )
#     tut_name = tutorial.text.lower()
#     if (' ' in tut_name):
#         tut_name = "_".join( tut_name.split() )
#     #file = name + "_" + str(tutorial_id) + ".html"
#     # if (lang == 'fr'):
#     #     file = name + "-" + tut_name + "_fr.html"
#     # else:    
#     #     file = name + "-" + tut_name + ".html"
#     file = name + "-" + tut_name + "_" + lang + ".html"
#     path = 'tutorials/' + file
#     context = {'tutorial': tutorial,'topics': topics,'file':file}
#     #context = {'tutorial': tutorial,'topics': topics}
#     #messages.warning(request, 'Made it to ps_tut view!')
#     return render(request, path, context)
# # for initial testing
# def powershell(request):
#     """Show all PowerShell Tutorials"""
#     tutorials = Tutorial.objects.filter(topic__text='Powershell').order_by('date_added')
#     context = {'tutorials': tutorials}
#     return render(request, 'tutorials/powershell/powershell.html', context)

# def scripting(request):
#     """Show all Linux Shell Scripting Tutorials"""
#     tutorials = Tutorial.objects.filter(topic__text='Shell Scripting').order_by('date_added')
#     context = {'tutorials': tutorials}
#     return render(request, 'tutorials/shell_scripting/shell_scripting.html', context)

# def network(request):
#     """Show all Networking Fundamentals Tutorials"""
#     tutorials = Tutorial.objects.filter(topic__text='Networking').order_by('date_added')
#     context = {'tutorials': tutorials}
#     return render(request, 'tutorials/networking/networking.html', context)

# def misc(request):
#     """Show all Miscellaneous Tutorials"""
#     tutorials = Tutorial.objects.filter(topic__text='Miscellaneous').order_by('date_added')
#     context = {'tutorials': tutorials}
#     return render(request, 'tutorials/miscellaneous/miscellaneous.html', context)
