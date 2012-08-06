from django.http import HttpResponse
from ecommerce.store.models import *
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import time 
from calendar import month_name

def index(request):
	page_title = 'Pursaholic Paradise'
	items = Item.objects.all()
	return render_to_response('index.html', locals())

def show_category(request, category_slug):
	c = get_object_or_404(Category, slug=category_slug)
	items = c.item_set.all()
	page_title = c.name
	return render_to_response('category.html', locals())

def show_item(request, item_slug):
	i = get_object_or_404(Item, slug=item_slug)
	categories = i.categories.filter(is_active=True)
	page_title = i.name
	return render_to_response('item.html', locals())

