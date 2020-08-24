from django.shortcuts import render
from django.contrib import messages

from .models import Topic, Tutorial

def powershell(request):
    """Show all PowerShell Tutorials"""
    tutorials = Tutorial.objects.filter(topic__text='Powershell').order_by('date_added')
    context = {'tutorials': tutorials}
    return render(request, 'tutorials/powershell/powershell.html', context)

def ps_tut(request, tutorial_id):
    tutorial = Tutorial.objects.get(id=tutorial_id)
    #file = request.POST['tut_id'] + ".html"
    file = str(tutorial_id) + ".html"
    path = 'tutorials/powershell/' + file
    #path = 'tutorials/powershell/1.html'
    context = {
        'tutorial': tutorial,
    }
    messages.warning(request, 'Made it to ps_tut view!')
    return render(request, path, context)
#     #return render(request, 'tutorials/topics/powershell/' + file, context)


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
