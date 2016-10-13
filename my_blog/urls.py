# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
# from article.views import RSSFeed
# from article.views import home
from article import views as article_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', article_views.home, name='home'),
    url(r'^(?P<id>[0-9].*)/$', article_views.detail, name='detail'),
    url(r'^archives/$', article_views.archives, name='archives'),
    url(r'^about/$', article_views.about, name='about'),
    url(r'^tag(?P<tag>\w+)/$', article_views.search_tag, name='search_tag'),
]