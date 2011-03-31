from modeltranslation.translator import translator, TranslationOptions
from catalog.models import Item

class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'entry', 'description',)

translator.register(Item, ItemTranslationOptions)