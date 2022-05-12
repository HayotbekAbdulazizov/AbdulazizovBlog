
from collections import defaultdict
from django.contrib.auth.models import User
from django.db.models import query
from rest_framework import fields, serializers
from rest_framework.relations import ManyRelatedField, SlugRelatedField, StringRelatedField
from .models import  DailyStory, StoryItem
from rest_framework.validators import UniqueForDateValidator, UniqueValidator, UniqueTogetherValidator


















class StoryItemSerializer(serializers.ModelSerializer):
    # articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # storyitems = serializers.HyperlinkedIdentityField(view_name='home')
    # storyitems = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    
    # title = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # slug = serializers.SlugField(allow_blank=True)  ## THIS allows you to edit existing model field      

    class Meta:
        model = StoryItem
        fields = ['story','title', 'file', 'date', 'date', 'type']
    # articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)








class DailyStorySerializer(serializers.ModelSerializer):
    # storyitems = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # storyitems = serializers.HyperlinkedIdentityField(view_name='home')
    # storyitems = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    
    # title = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # slug = serializers.SlugField(allow_blank=True)  ## THIS allows you to edit existing model field      
    storyitems = StoryItemSerializer(many=True, read_only=True)

    class Meta:
        model = DailyStory
        fields = ['title', 'slug', 'preview', 'date','storyitems']
    # articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)







