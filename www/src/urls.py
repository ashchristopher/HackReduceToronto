from django.conf.urls.defaults import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^app/', include('app.foo.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('mapreduce.urls')),
    url(r'^site-media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }, name='media'),
)
