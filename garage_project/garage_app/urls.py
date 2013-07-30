from django.conf.urls import patterns, url

from garage_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^doors/(?P<door_id>\d+)/update/$', views.update, name='update'),
	url(r'^doors/(?P<door_id>\d+)/open/$', views.update, name='open'),
	url(r'^doors/(?P<door_id>\d+)/close/$', views.update, name='close'),
)
