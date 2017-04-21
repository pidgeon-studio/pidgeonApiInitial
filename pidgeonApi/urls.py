from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^sms/send$', 'pidgeonApi.sms.views.send'),
]
