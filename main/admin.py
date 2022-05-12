from attr import field
from django.contrib import admin
from .models import DailyStory, StoryItem

# Register your models here.
class StoryItemInline(admin.StackedInline):
    model = StoryItem

class DailyStoryAdmin(admin.ModelAdmin):
    inlines = [StoryItemInline,]


admin.site.register(DailyStory)
admin.site.register(StoryItem)