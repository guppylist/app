from django.views.generic import TemplateView, DetailView

from list.models import List


class ListListView(TemplateView):
    template_name = 'list/list.html'


class ListDetailView(DetailView):
    template_name = 'list/details.html'
    model = List
