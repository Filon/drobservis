from django.contrib import admin
from models import Page
from feincms.admin import editor

class PageAdmin(editor.TreeEditor):
    list_display = ('title',)


admin.site.register(Page, PageAdmin)