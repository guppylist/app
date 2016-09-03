from django.conf.urls import url

from list.views import ListListView, ListDetailView


urlpatterns = [
    url(r'^$', ListListView.as_view()),
    url(r'^(?P<pk>[^\.^/]+)/$', ListDetailView.as_view(), name='list_details'),
]