from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('guppylist.contrib.search.urls')),
    url(r'^products/', include('guppylist.contrib.product.urls')),
    url(r'^lists/', include('guppylist.contrib.list.urls')),
    url(r'^u/(?P<username>[^\.^/]+)/$', 'guppylist.contrib.list.views.lists'),
    url(r'^u/(?P<username>[^\.^/]+)/list/(?P<list_slug>[^\.^/]+)$', 'guppylist.contrib.list.views.list'),
    url(r'^$', 'guppylist.contrib.page.views.home'),
    # url(r'^(?P<slug>[^\.^/]+)/$', view),
)