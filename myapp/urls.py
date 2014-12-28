__author__ = 'aliuzun'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('myapp.views',
    url(r'^$', 'home', name='home'),
    url(r'^list', 'list', name='list'),
)