#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _ 


urlpatterns = [
    #url(r'^$', views.main),
    #url(r'^#start/(?P<lang_code>)/$', views.main),
    #url(r'^#info/(?P<lang_code>)/$', views.main),
    #url(r'^#idea/(?P<lang_code>)/$', views.main),
    #url(r'^#data/(?P<lang_code>)/$', views.main),
    #url(r'^#contact/(?P<lang_code>)/$', views.main),
    url(r'^#start', views.main),
    url(r'^#info', views.main),
    url(r'^#idea/$', views.main),
    url(r'^#data/$', views.main),
    url(r'^#contact/$', views.main),
    url(r'^#start/en/$', views.main),
    url(r'^/mail', views.send_email),
]

