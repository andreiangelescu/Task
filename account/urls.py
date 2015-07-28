from __future__ import print_function

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import create_user, login_user, logout_user, RegisterConfirm2Ways, ActivationComplete

urlpatterns = patterns('',
	#url(r'^$', index ),
	url(r'^create_user/$', create_user, name='create_user' ),
	url(r'^login_user/$', login_user, name='login_user'),
	url(r'^logout_user/$', logout_user, name='logout_user'),
	url(r'^account_verification/$', RegisterConfirm2Ways.as_view(), name='account_verification'),
	url(r'^account_verification/(?P<activation_key>\w+)/', RegisterConfirm2Ways.as_view(), name='account_verification'),
	url(r'^activation_complete/', ActivationComplete.as_view(),name='activation_complete'),
)