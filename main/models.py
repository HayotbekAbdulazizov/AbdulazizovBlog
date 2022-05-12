from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.

class DailyStory(models.Model):
    title = models.CharField('title', max_length=100)
    slug = models.SlugField('*', unique=True, blank=True)
    preview = models.ImageField("Image Preview", upload_to ='preview-images/%Y/%m/%d/', blank=True)
    # video = models.FileField('Document', upload_to='story-documents/% Y/% m/% d/')
    date = models.DateField('Date',)
    # time = models.TimeField('Time', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'


class StoryItem(models.Model):
    TYPES = [
        ('video', 'video'),
        ('photo', 'photo'),
    ]

    story = models.ForeignKey(DailyStory, on_delete=models.CASCADE, related_name='storyitems',blank=True)
    title = models.CharField('Story Item Title', max_length=200, blank=True)
    type = models.CharField(max_length=100,choices=TYPES,default="video",)
    file = models.FileField('File', upload_to='story-files/%Y/%m/%d/', blank=True)
    date = models.DateTimeField('Date Time', blank=True)

    def __str__(self):
        return f"{self.story} - {self.title}"

    class Meta:
        verbose_name = 'StoryItem'
        verbose_name = 'StoryItems'