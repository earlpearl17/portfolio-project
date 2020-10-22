from django.contrib import admin

from tutorials.models import Topic, Tutorial

@admin.register(Topic)
#admin.site.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    # list_display = ("text", "date_added")
    list_display = ("id", "text", "date_added")


@admin.register(Tutorial)
#admin.site.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    # list_display = ("text", "topic", "lang", "date_added")
    list_display = ("id", "text", "topic", "type", "lang", "date_added")
