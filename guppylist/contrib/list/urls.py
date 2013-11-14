from django.conf.urls import *
from guppylist.contrib.list.views import *

urlpatterns = patterns('guppylist.contrib.list.views',
    # url(r'^(?P<slug>[^\.^/]+)/$', view),
    url(r'add/submit/$', add_submit),
)