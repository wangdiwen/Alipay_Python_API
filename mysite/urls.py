#!/usr/bin/env python

# import django env
from django.conf.urls import patterns, include, url

# urls conf
urlpatterns = patterns('',  # init instance
    # web site urls
    # url(r'^admin/', include('application.backend.urls')),
    # url(r'^about/', include('application.about.urls')),
    # url(r'^', include('application.frontend.urls')),
    url(r'^', include('application.zhi.urls')),
)
