# -*- coding: utf-8 -*-

from django.conf.urls import *
from tastypie.api import Api
from apps.notifications.resource import NotificationResource

api = Api('notification')
api.register(NotificationResource())


urlpatterns = patterns('apps.notifications.views',
    url(r'^$', 'all', name='all'),
    url(r'^unread/$', 'unread', name='unread'),
    url(r'^mark-all-as-read/$', 'mark_all_as_read', name='mark_all_as_read'),
    url(r'^mark-as-read/(?P<slug>\d+)/$', 'mark_as_read', name='mark_as_read'),
    url(r'^mark-as-unread/(?P<slug>\d+)/$', 'mark_as_unread', name='mark_as_unread'),
)
