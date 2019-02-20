#-*- coding:utf-8 -*-
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', index),
    url(r'rich_content/$', rich_content),
]