#-*- coding: utf-8 -*-
"""sfugd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from mainpage import views
from mainpage.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^email', views.send_email),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt.html'), name="robots"),
]

urlpatterns += i18n_patterns(
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'\S+', views.main_check),
    url(r'', views.main, name='right_entrance'),
)





    
