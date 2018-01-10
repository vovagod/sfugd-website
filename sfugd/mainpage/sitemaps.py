from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from mainpage.models import Menu_one

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    i18n = True

    def items(self):
         return ['right_entrance']

    def location(self, item):
        return reverse(item)
