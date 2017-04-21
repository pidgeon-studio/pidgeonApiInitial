from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^sms/send$', 'pidgeonApi.sms.views.send'),
]
