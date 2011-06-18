from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# booking type 
urlpatterns = patterns('mapreduce.views',
    url(r'^$', 'index', {}, name='index'),
)
