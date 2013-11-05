from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from guppylist.contrib.page.forms import SignupForm

def home(request):
    form = SignupForm()
    payload = dict(form=form)
    return render_to_response('page/home.html', payload, context_instance=RequestContext(request))