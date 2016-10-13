# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

from django.contrib.syndication.views import Feed

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from article.models import Article
#from article.models import Tag

from datetime import datetime


# Create your views here.
def home(request):
    post_list = Article.objects.all()
    #return HttpResponse("Hello World, Django")
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, my_args):
    post = Article.objects.filter(id=int(my_args))[0]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)