from django.conf.urls.defaults import patterns, include, url
from django.http import HttpResponseRedirect
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'cross.views.home'),
    url(r'^moreinfo$', 'cross.views.moreinfo'),
    url(r'^getinvolved$', 'cross.views.getinvolved'),
    url(r'^contact$', 'cross.views.contact'),
    url(r'^mailingadd', 'cross.views.mailingadd'),
    # url(r'^Crossing/', include('Crossing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
