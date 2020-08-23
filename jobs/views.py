from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def powershell(request):
    return render(request, 'jobs/powershell.html')

def scripting(request):
    return render(request, 'jobs/shell_scripting.html')

def network(request):
    return render(request, 'jobs/networking.html')

def misc(request):
    return render(request, 'jobs/miscellaneous.html')