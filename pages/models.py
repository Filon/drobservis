# -*- coding: utf-8 -*-

from django.db import models
import mptt

class Page(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, db_index=True)
    content = models.TextField(blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        url = self.slug
        page = self.parent
        while page:
            url = page.slug + '/' + url
            page = page.parent
        return '/' + url
    
    def get_breadcrumbs(self):
        breadcrumbs = []
        page = self
        while page:
            breadcrumbs.append({'title': page.title, 'url': page.get_absolute_url()})
            page = page.parent
        breadcrumbs.append({'title': 'Главная', 'url': '/'})
        breadcrumbs.reverse()
        return breadcrumbs
        
    
    
mptt.register(Page)