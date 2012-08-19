from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from ecommerce.accounts.models import Order, OrderItem, UserProfile
from ecommerce.accounts.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from ecommerce.store.models import Item
from django.core.exceptions import ObjectDoesNotExist
from ecommerce.store.forms import AddItem
from django.template.defaultfilters import slugify

@login_required
def my_account(request, template_name="registration/my_account.html"):
	page_title = "My Account"
	name = request.user.username
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def my_orders(request, template_name="registration/my_orders.html"):
	user_items = Item.objects.filter(user=request.user)
	order_items = OrderItem.objects.filter(item__in=user_items)
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
	
@login_required
def order_info(request, template_name="registration/order_info.html"):
	if request.method == 'POST':
		postdata = request.POST.copy()
		form = CustomerForm(postdata)
		if form.is_valid():
			profile.set(request)
			url = urlresolvers.reverse('my_account')
			return HttpResponseRedirect(url)
	else:
		try:
			u = UserProfile.objects.get(user=request.user)
			form = UserProfileForm(instance=u)
			page_title = 'Edit Order Information'
		except ObjectDoesNotExist:
				form = UserProfileForm()
		return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def update_settings(request):
	if request.method== 'POST':
		try:
			u = UserProfile.objects.get(user=request.user)
			form = UserProfileForm(request.POST, instance=u)
		except ObjectDoesNotExist:
			form = UserProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return render_to_response('registration/settings_update_complete.html')
	else:
		try:
			u = UserProfile.objects.get(user=request.user)
			form = UserProfileForm(instance=u)
		except ObjectDoesNotExist:
			form = UserProfileForm()
		return render_to_response('registration/update_settings.html', locals(), context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return render_to_response("registration/logged_out.html", locals())

def my_listed_items(request):
	items_selling = Item.objects.filter(user=request.user)
	return render_to_response('my_listed_items.html', locals(), context_instance=RequestContext(request))

def my_purchases(request):
	my_orders = Order.objects.filter(buyer=request.user)
	my_items = OrderItem.objects.filter(order__in=my_orders)
	return render_to_response('my_purchases.html', locals())

def order_details(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	order_items = OrderItem.objects.filter(order=order)
	return render_to_response('order_details.html', locals(),
	context_instance=RequestContext(request))

def delete_item(request, item_id):
	if request.method =='POST':
		item = Item.objects.get(id=item_id)
		if item.user == request.user:
			item.delete()
			items_selling = Item.objects.filter(user=request.user)
			return render_to_response('my_listed_items.html', locals(), context_instance=RequestContext(request))
	else:
		return render_to_response('delete.html', locals(), context_instance=RequestContext(request))
				
def edit_item(request, item_id):
	if request.method == 'POST':
		item = Item.objects.get(id=item_id)
		form = AddItem(request.POST,instance=item)
		if form.is_valid():
			item = form.save(commit=False)
			item.user = request.user
			item.is_active = True
			item.slug = slugify(item.name)
			item.save()
			return HttpResponseRedirect('thanks.html')
		else:
			form = AddItem(instance=item )
			return render_to_response('forsale.html', locals(), context_instance=RequestContext(request))
	else:
		item = Item.objects.get(id=item_id)
		form = AddItem(instance=item)
		return render_to_response('forsale.html', locals(), context_instance=RequestContext(request))