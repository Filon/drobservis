from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=250)
    alias = models.SlugField()

class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=500)
    order = models.IntegerField(default=0)
    
    menu = models.ForeignKey(Menu)    
    
