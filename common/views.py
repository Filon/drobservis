from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from models import Menu, MenuItem

def menu(request):
    main_menu_id = get_object_or_404(Menu, alias='main-menu')
    main_menu = MenuItem.objects.filter(menu=main_menu_id).order_by('order')
    
    footer_menu_id = get_object_or_404(Menu, alias='footer-menu')
    footer_menu = MenuItem.objects.filter(menu=footer_menu_id).order_by('order')
    
    return {'main_menu': main_menu, 'footer_menu': footer_menu}
    return {}

def page(request): 
    t = get_template('common/menu.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))