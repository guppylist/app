from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from guppylist.contrib.list.models import List
from guppylist.contrib.list.forms import ListForm
from guppylist.contrib.product.models import Product

def add_submit(request):
    if request.method == 'POST':
        form = ListForm(request.POST)

        if form.is_valid():
            list = List()
            list.title = form.cleaned_data['title']
            list.description = form.cleaned_data['description']
            list.user = request.user
            list.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    payload = dict()
    return render_to_response('product/view.html', payload, context_instance=RequestContext(request))