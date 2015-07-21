from __future__ import print_function

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import add_task, task_list, edit_task, delete_tasks, edit_in_place

urlpatterns = patterns('',
	#url(r'^$', index ),
	url(r'^tasks/$', task_list , name='tasks'),
	url(r'^add/$', add_task, name='add'), # add prin form
	url(r'^edit/$', edit_task, name='edit'),
	#url(r'^task/(?P<pk>[0-9]+)/$', add_task, name='detail'),
	url(r'^edit/(?P<pk>[0-9]+)/$', edit_task, name='edit'), #editate prin form
	#url(r'^task_edit/(?P<pk>[0-9]+)/$', edit_task),
	url(r'^delete/(?P<pk>[0-9]+)/$', delete_tasks, name='delete'),
	url(r'^edit_in_page/$', edit_in_place, name='edit_in_page'),  #editare automata
	#url(r'^editp/(?P<pk>[0-9]+)/$', edit_in_place, name='editp'),
	#url(r'^browse/$', browse_by_name, name='browse'),
	
)


