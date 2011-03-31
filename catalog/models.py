from django.db import models
import mptt

class Item(models.Model):
    name = models.CharField(max_length=250)
    entry = models.TextField(blank=True)
    description = models.TextField(blank=True)
    
    draft = models.CharField(max_length=250, blank=True)
    coordinates = models.TextField(blank=True)
    
    is_detail = models.BooleanField(default=True)
    is_page = models.BooleanField(default=True)
    
    order = models.IntegerField(default=0)
    
    parent = models.ForeignKey('self', null=True, blank=True)
    
    def __unicode__(self):
        if self.draft:
            return u"%s - %s" % (self.name, self.draft)
        else:
            return self.name
    
    def get_full_url(self):
        return u'/catalog/%s' % self.id


mptt.register(Item)