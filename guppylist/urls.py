from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^search/' include('guppylist.contrib.search.urls')),
    # url(r'^$', 'guppylist.contrib.page.views.home'),
)
