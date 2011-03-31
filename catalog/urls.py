# -*- coding: utf-8 -*-
# encodig: utf-8

from django.conf.urls.defaults import * #@UnusedWildImport
from views import main, category

urlpatterns = patterns('',
    (r'^$', main),
    (r'^/(?P<id>\d+)$', category),
)
