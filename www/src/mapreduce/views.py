from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse


def index(request, template='mapreduce/index.html'):
    context = {'data_id': request.GET.get('data_id', '')}
    return render_to_response(template, context, context_instance=RequestContext(request))
