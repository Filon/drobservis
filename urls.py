# -*- coding: utf-8 -*-

from django.conf.urls.defaults import * #@UnusedWildImport
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    
    (r'^favicon.ico$', 'common.views.page'),
    (r'^$', 'catalog.views.main'),
    (ur'Каталог', include('catalog.urls')),
    #(r'', include('pages.urls')),
)
