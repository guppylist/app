from django.conf.urls import *
from guppylist.contrib.product.views import *

urlpatterns = patterns('guppylist.contrib.product.views',
    url(r'^(?P<slug>[^\.^/]+)/$', view),
)