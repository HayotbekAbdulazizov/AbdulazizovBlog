from django.shortcuts import render
from django.template.response import TemplateResponse
from django.template import context
from django.views import View
from django.views.generic import MonthArchiveView, CreateView
from .models import DailyStory, Post, StoryItem

import json
from django.core import serializers
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import DailyStorySerializer, StoryItemSerializer







# from djpjax import pjax, PJAXResponseMixin

# @pjax()
def home(request):
    # posts = Post.objects.all().order_by("-date")
    # stories = DailyStory.objects.all().order_by("-date")
    # story_items = StoryItem.objects.all().order_by("-date")
    # stories_json = DailyStorySerializer(stories, many=True)
    # story_items_json = StoryItemSerializer(story_items, many=True)

    context = {
    #     "posts":posts,
    #     "stories":stories,
    #     "stories_items":story_items,
    #     "stories_json":json.dumps(stories_json.data),
    #     "story_items_json":json.dumps(story_items_json.data),
    }

    return render(request, "index.html", context)


def about(request):
    # posts = Post.objects.all().order_by("-date")
    # stories = DailyStory.objects.all().order_by("-date")
    # story_items = StoryItem.objects.all().order_by("-date")
    # stories_json = DailyStorySerializer(stories, many=True)
    # story_items_json = StoryItemSerializer(story_items, many=True)

    context = {
        # "posts":posts,
        # "stories":stories,
        # "stories_items":story_items,
        # "stories_json":json.dumps(stories_json.data),
        # "story_items_json":json.dumps(story_items_json.data),
        "status":200,
    }

    return render(request, "site_base2.html", context)








def test(request):
    # posts = Post.objects.all().order_by("-date")
    # stories = DailyStory.objects.all().order_by("-date")
    # story_items = StoryItem.objects.all().order_by("-date")
    # stories_json = DailyStorySerializer(stories, many=True)
    # story_items_json = StoryItemSerializer(story_items, many=True)

    context = {
        # "posts":posts,
        # "stories":stories,
        # "stories_items":story_items,
        # "stories_json":json.dumps(stories_json.data),
        # "story_items_json":json.dumps(story_items_json.data),
        "status":200,
    }

    return render(request, "test.html", context)














# class HomePageView(GenericAPIView, View):
#     def get(self, request):
#         posts = Post.objects.all().order_by("-date")
#         stories = DailyStory.objects.all().order_by("-date")
#         story_items = StoryItem.objects.all().order_by("-date")
#         stories_json = DailyStorySerializer(stories, many=True)
#         story_items_json = StoryItemSerializer(story_items, many=True)

#         # Post.objects.create()



#         context = {
#             "posts":posts,
#             "stories":stories,
#             "stories_items":story_items,
#             "stories_json":json.dumps(stories_json.data),
#             "story_items_json":json.dumps(story_items_json.data),
#         }
        # return render(request, 'index.html', context=context)
        





# def postDetailView(request, post_slug):
	# context = {
		# 'post':post_slug,
	# }
	# return render(request, 'post_detail.html', context)
# @pjax()
def postDetailView(request, post_slug):
    return TemplateResponse(request, "post_detail.html", {'post':post_slug})

        
        



































































































# from parler.views import ViewUrlMixin, TranslatableUpdateView
# from parler.utils.context import switch_language

# class ArticleEditView(ViewUrlMixin, TranslatableUpdateView):
#     view_url_name = 'article:edit'

#     def get_view_url(self):
#         with switch_language(self.object, get_language()):
#             return reverse(self.view_url_name, kwargs={'slug': self.object.slug})


























































# Trash


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

