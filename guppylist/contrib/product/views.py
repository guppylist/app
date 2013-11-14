from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from guppylist.contrib.product.models import Product
from guppylist.contrib.list.models import List
from guppylist.contrib.list.forms import ListForm

def view(request, slug):
    form = ListForm()
    product = Product.get_product(slug)
    lists = List.objects.filter(user=request.user)
    request.page_title = product.data.title

    payload = dict(product=product, form=form, lists=lists)
    return render_to_response('product/view.html', payload, context_instance=RequestContext(request))