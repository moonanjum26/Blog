from django.conf.urls import url
from .views import (

     post_list,
	 post_create,
	 post_detail,
	 post_update,
	 post_delete
)



urlpatterns = [
    url(r'^$', post_list, name='list'),
	url(r'^create/$', post_create, name='create'),
	url(r'^(?P<id>[0-9]+)/$', post_detail, name='detail'),
	url(r'^(?P<id>[0-9]+)/edit/$', post_update, name='update'),
	url(r'^(?P<id>[0-9]+)/delete/$', post_delete, name='delete'),
]