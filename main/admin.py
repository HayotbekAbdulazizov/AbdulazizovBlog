from django.contrib import admin

from main.forms import PostAdminForm
from .models import DailyStory, StoryItem, Category, Tag, Post, PostImage

class StoryItemStacked(admin.StackedInline):
    model = StoryItem
    extra = 1    

class PostImageStacked(admin.StackedInline):
    model = PostImage
    extra = 1    



class DailyStoryAdmin(admin.ModelAdmin):
    inlines = [StoryItemStacked,]
    list_display = ('title',  "date", "id")
    list_display_links = ("title", "date","id")
    prepopulated_fields = {'slug':('title',), 'slug_en':('title_en',),'slug_uz':('title_uz',),'slug_ru':('title_ru',) }


class StoryItemAdmin(admin.ModelAdmin):
    list_display = ('story','title',  "date", "id")
    list_display_links = ("story","title", "date","id")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', "id")
    list_display_links = ("name", "id")
    prepopulated_fields = {'slug':('name',), 'slug_en':('name',),'slug_uz':('name',),'slug_ru':('name',) }





class TagAdmin(admin.ModelAdmin):
    list_display = ('name', "id")
    list_display_links = ("name","id")
    prepopulated_fields = {'slug':('name',), 'slug_en':('name_en',),'slug_uz':('name_uz',),'slug_ru':('name_ru',) }



class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    inlines = [PostImageStacked,]
    list_display = ('category',  "title", "author")
    list_display_links = ('category',  "title", "author")
    prepopulated_fields = {'slug':('title',), 'slug_en':('title_en',),'slug_uz':('title_uz',),'slug_ru':('title_ru',) }




class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', "id")
    list_display_links = ("post","id")





admin.site.register(DailyStory,DailyStoryAdmin)
admin.site.register(StoryItem, StoryItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)