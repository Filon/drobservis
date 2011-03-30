from django.conf.urls.defaults import *
from views import main

urlpatterns = patterns('',
    (r'^(?P<url>.*)$', main),
)