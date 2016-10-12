# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
#from article.views import RSSFeed
#from article.views import home
from article import views as article_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', article_views.home),
    url()
#    url(r'^(?Pd+)/$', article_views.detail, name='detail'),
]
