import json
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from guppylist.contrib.product.models import Product

def index(request):
    q = ''
    products = []
    request.page_title = 'Product Search'

    if request.GET.get('q'):
        q = request.GET.get('q')
        products = Product.search(q)
        request.page_title = q


    payload = dict(q=q, products=products)
    return render_to_response('search/index.html', payload, context_instance=RequestContext(request))

def data_search(request):
    q = ''

    products = []
    if request.GET.get('q'):
        q = request.GET.get('q')
        results = Product.search(q)

        for product in results:
            products.append(product.filter_api())

    payload = dict(q=q, products=products)
    return HttpResponse(json.dumps(payload), mimetype='application/json')