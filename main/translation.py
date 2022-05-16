from modeltranslation.translator import translator, TranslationOptions
from .models import DailyStory, PostImage, StoryItem,Category,Tag,Post


class DailyStoryTranslationOptions(TranslationOptions):
    fields = ('title', 'slug','preview')



class StoryItemTranslationOptions(TranslationOptions):
    fields = ( 'title', 'file')



class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','slug' )



class TagTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'image')



class PostTranslationOptions(TranslationOptions):
    fields = ( 'title', 'slug', 'author', 'body' )


class PostImageTranslationOptions(TranslationOptions):
    fields = ('file', )





translator.register(DailyStory , DailyStoryTranslationOptions)
translator.register(StoryItem , StoryItemTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Post , PostTranslationOptions)
translator.register(Tag , TagTranslationOptions)
translator.register(PostImage , PostImageTranslationOptions)