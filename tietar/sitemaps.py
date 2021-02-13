from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['index', 'produccion', 'servicios', 'galeria']

    def location(self, item):
        return reverse(item)