from django.contrib import admin
from models import Item
from feincms.admin import editor
from modeltranslation.admin import TranslationAdmin
    
class ItemAdmin(editor.TreeEditor):    
    list_display = ('name', 'draft', 'is_detail', 'is_page')
    search_fields = ('name',)
    list_filter = ('is_page', 'is_detail',)
    list_per_page = 100000
    
class TranslatedItemAdmin(ItemAdmin, TranslationAdmin):
    class Media:
        js = (
            '/media/modeltranslation/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/media/modeltranslation/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/media/modeltranslation/tabbed_translation_fields.css',),
        }
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(TranslatedItemAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field

admin.site.register(Item, TranslatedItemAdmin)
