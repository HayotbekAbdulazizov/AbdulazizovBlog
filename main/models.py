from django.db import models    
from django.utils.translation import gettext as _
from django.urls import reverse
# Create your models here.






# Class DailyStory stories and news sections
class DailyStory(models.Model):
    title = models.CharField('title', max_length=100)
    slug = models.SlugField('slug', unique=True, blank=True)
    preview = models.ImageField("Image Preview", upload_to ='preview-images/%Y/%m/%d/', blank=True)
    date = models.DateField('Date',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'






# Class Story items model connected to DailyStory 
class StoryItem(models.Model):
    TYPES = [(_('video'), _('video')),(_('photo'), _('photo')),]
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











# Category model
class Category(models.Model):
    name = models.CharField("Name", max_length=200, blank=True)
    slug = models.SlugField("*", max_length=200, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"







 # Tag model
class Tag(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = models.SlugField("*", unique=True, blank=True)
    image = models.ImageField('Image', upload_to="Tag-images/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"    
        verbose_name = "Tags"    









class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True)
    title = models.CharField('Title', max_length=400, blank=True)
    slug = models.SlugField("*", unique=True, blank=True)
    body = models.TextField(blank=True,)
    author = models.CharField("Author Name", max_length=400, blank=True)
    tags = models.ManyToManyField(Tag,related_name='posts', blank=True)
    likes = models.PositiveIntegerField("Likes", default=0 )
    views = models.PositiveIntegerField('Views', default=0)
    date = models.DateTimeField('Date', blank=True, auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} - {self.title}"

    def get_absolute_url(self):
        return reverse('main:post_detail', kwargs={'post_slug':self.slug})

    class Meta:
        verbose_name = "Post"
        verbose_name = "Posts"




class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postimages')
    file = models.FileField('File', upload_to='Post-previews/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.post.category.name

    class Meta:
        verbose_name = 'Post Image'
        verbose_name_plural = 'Post Images'