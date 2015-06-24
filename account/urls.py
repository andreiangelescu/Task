from __future__ import print_function

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import create_user, login_user, logout_user

urlpatterns = patterns('',
	#url(r'^$', index ),
	url(r'^create_user/$', create_user, name='create_user' ),
	url(r'^login_user/$', login_user, name='login_user'),
	url(r'^logout_user/$', logout_user, name='logout_user'),
)