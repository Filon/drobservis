from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse

from models import Item

def main(request):
    items = Item.objects.filter(level=0)
    for item in items:
        item.childs = Item.objects.filter(level=1, parent=item, is_page=True)
    
    t = get_template('catalog/index.html')
    c = RequestContext(request, {'items': items})
    return HttpResponse(t.render(c))
    
def category(request, id):
    item = get_object_or_404(Item, id=id)
    childs = item.get_children()
    
    t = get_template('catalog/category.html')
    c = RequestContext(request, {'item': item, 'childs': childs})
    return HttpResponse(t.render(c))