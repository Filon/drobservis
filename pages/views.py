# -*- coding: utf-8 -*-

from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse, Http404
from models import Page

def main(request, url):
    pages = Page.objects.all()
    page = None
    for p in pages:
        if p.get_absolute_url()[1:] == url:
            page = p
            break 
    
    if page:
        t = get_template('pages/index.html')
        c = RequestContext(request, {'page': page})
        return HttpResponse(t.render(c))
    else:
        raise Http404