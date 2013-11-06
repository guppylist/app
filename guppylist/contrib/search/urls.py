from django.conf.urls import *
from guppylist.contrib.search.views import *

urlpatterns = patterns('guppylist.contrib.search.views',
    url('', view=index),
)