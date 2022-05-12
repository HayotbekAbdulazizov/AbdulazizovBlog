from typing import List
from django.shortcuts import render
from django.template import context
from django.views import View
from django.views.generic import MonthArchiveView
from .models import DailyStory, StoryItem

import json
from django.core import serializers
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import DailyStorySerializer, StoryItemSerializer






class HomePageView(GenericAPIView, View):
    def get(self, request):
        stories_all = DailyStory.objects.all().order_by("-date")
        storiy_item_all = StoryItem.objects.all().order_by("-date")
        stories = DailyStorySerializer(stories_all, many=True)
        story_items = StoryItemSerializer(storiy_item_all, many=True)

        context = {
            'stories_all':stories_all,
            "stories":json.dumps(stories.data),
            # 'stories':stories,
            'story_items':json.dumps(story_items.data),
        }
        return render(request, 'index.html', context=context)
        
        


    # result = {}
    # for sample in stories_all:
    #     date_string = sample.date.strftime("%m.%d.%Y")
    #     if date_string in result:
    #         result[date_string].append(sample)
    #     else:
    #         result[date_string] = [sample]

    # stories = serializers.serialize("json", stories_all)
    # story_items = serializers.serialize("json", storiy_item_all, fields=["story","title","file","date" ])

    # context = {
    #     'date_list':result,
    #     "stories":json.dumps(stories),
    #     'stories':stories,
    #     'story_items':story_items,
    # }
    # st = json.dump(people, context)











# queryset = MyModel.objects.annotate(
#     created_at_date=TruncDate('created_at'),
# ).order_by('created_at')
# groupedset = groupby(queryset, attrgetter('created_at_date'))


#   console.log('--- Stories')
    # for (let i = 0; i < result.length; i++) {
    #   console.log(result[i]['pk'])
    #   let element = result[i]['pk'];
    #   console.log(story_items[])
    #   // let storyitem = story_items['pk']
      
    # }
#   // console.log(x['pk'])

