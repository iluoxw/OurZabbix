# coding:utf-8

from django.conf.urls import include,url
from views import *

urlpatterns = [
    url(r'^save_cpu$', saveCpu),
]