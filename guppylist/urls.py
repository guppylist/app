from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('guppylist.contrib.search.urls')),
    url(r'^lists/', include('guppylist.contrib.list.urls')),
    # url(r'^u/(?P<username>[^\.^/]+)/$', 'guppylist.contrib.list.views.lists'),
    # url(r'^u/(?P<username>[^\.^/]+)/list/(?P<list_slug>[^\.^/]+)$', 'guppylist.contrib.list.views.list'),
    url(r'^$', 'guppylist.contrib.page.views.home'),
    # url(r'^(?P<slug>[^\.^/]+)/$', view),
    url(r'api/util/metadata/$', 'guppylist.contrib.list.views.get_metadata'),
    url(r'item/add/$', 'guppylist.contrib.list.views.item_add'),
    url(r'item/(?P<id>[^\.^/]+)/$', 'guppylist.contrib.list.views.item_view'),
)