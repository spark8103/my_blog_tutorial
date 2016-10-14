from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title.encode('utf-8')

    def __unicode__(self) :
        return self.title

    class Meta: 
        ordering = ['-date_time']