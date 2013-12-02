from django.conf.urls import *
from guppylist.contrib.list.views import *

urlpatterns = patterns('guppylist.contrib.list.views',
    url(r'add/test/$', test_form),
    url(r'add/new/submit/$', add_new_submit),
    url(r'add/existing/submit/$', add_existing_submit),
    url(r'add/form/$', add_form),
    url(r'$', lists),
)