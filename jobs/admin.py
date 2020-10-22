from django.contrib import admin

#from .models import Job
# admin.site.register(Job)

from jobs.models import Job

@admin.register(Job)

class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type")
