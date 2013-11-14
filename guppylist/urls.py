from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('guppylist.contrib.search.urls')),
    url(r'^product/', include('guppylist.contrib.product.urls')),
    url(r'^list/', include('guppylist.contrib.list.urls')),
    url(r'^$', 'guppylist.contrib.page.views.home'),
)