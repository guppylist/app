import json
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from guppylist.contrib.product.models import Product
from guppylist.contrib.list.views import add_form
from guppylist.contrib.list.models import List
from guppylist.contrib.list.forms import ListAddNewForm, ListAddExistingForm

def view(request, slug):
    product = Product.get_product_by_slug(slug)

    lists = []
    add_product_to_list_form = ''
    if request.user.is_authenticated():
        lists = List.objects.filter(user=request.user)
        add_product_to_list_form = add_form(request, product, lists).content

        request.scripts['list'] = {
            'productId': int(product.id),
            'addProductToListForm': json.dumps(add_product_to_list_form),
            'lists': json.dumps([{'id': list.id, 'title': list.title} for list in lists]),
        }

    # Add request elements for the template.
    request.page_title = product.data.title

    payload = dict(
        product=product,
        add_product_to_list_form=add_product_to_list_form,
        lists=lists,
    )
    return render_to_response('product/view.html', payload, context_instance=RequestContext(request))