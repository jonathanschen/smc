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
from django.core import urlresolvers
from ecommerce.cart import cart
from django.http import HttpResponseRedirect
from ecommerce.store.forms import ItemAddToCartForm
from ecommerce.accounts.models import UserProfile
from ecommerce.store.forms import AddItem
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth import logout
from ecommerce.store.forms import ContactForm
from django.contrib.auth.decorators import login_required

def index(request):
	page_title = 'TaiDai Heaven'
	items = Item.objects.all().order_by("-created")
	paginator = Paginator(items, 12)
	
	try: 
		page = int(request.GET.get("page", "1"))
	except ValueError: 
		page = 1
	
	try:
		items = paginator.page(page)
	except:
		items = paginator.page(paginator.num_pages)
		
	return render_to_response('index.html', locals(), context_instance=RequestContext(request))

@login_required
def sell(request):
	if request.method == "POST":
		form = AddItem(request.POST, request.FILES)
		if form.is_valid():
			item = form.save(commit=False)
			item.user = request.user
			item.is_active = True
			item.slug = slugify(item.name)
			item.save()
			return render_to_response('thanks.html')	
	else:
		form = AddItem()
	return render_to_response('forsale.html', locals(), context_instance=RequestContext(request))
	
def blog(request):
	return render_to_response('blog.html')

def show_category(request, category_slug):
	c = get_object_or_404(Category, slug=category_slug)
	items = c.item_set.all()
	page_title = c.name
	return render_to_response('category.html', locals(), context_instance=RequestContext(request))

def show_item(request, item_slug):
	item = get_object_or_404(Item, slug=item_slug)
	categories = item.categories.all()
	page_title = item.name
	if request.method == 'POST':
		postdata = request.POST.copy()
		form = ItemAddToCartForm(request, postdata)
		if form.is_valid():
			cart.add_to_cart(request)
			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()
			url = urlresolvers.reverse('show_cart')
			return HttpResponseRedirect(url)
	else:
		form = ItemAddToCartForm(request=request, label_suffix=':')
	form.fields['item_slug'].widget.attrs['value'] = item_slug
	request.session.set_test_cookie()
	return render_to_response('item.html', locals(), context_instance=RequestContext(request))

def contact(request):	
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			message = form.cleaned_data['message']
			email = form.cleaned_data['email']

			recipients = ['jonathanschen@gmail.com']
			send_mail(name, message, email, recipients)	
			return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form':form,})


