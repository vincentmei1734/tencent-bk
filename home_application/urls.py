# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'helloworld'),
    (r'^mwptest1/$','mwptest1'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^home$', 'home'),
    (r'^test/$', 'test'),
)