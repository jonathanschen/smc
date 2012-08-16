from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from ecommerce.accounts.models import Order, OrderItem, UserProfile
from ecommerce.accounts.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ecommerce.store.models import Item


@login_required
def my_account(request, template_name="registration/my_account.html"):
	page_title = "My Account"
	orders = Order.objects.filter(user=request.user)
	name = request.user.username
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def order_details(request, template_name="registration/order_details.html"):
	order = get_object_or_404(Order, id=order_id, user=request.user)
	page_title = "Order Details for Order #" + order_id
	order_items = OrderItem.objects.filter(order=order)
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
			user_profile = profile.retrieve(request)
			form = CustomerForm(instance=user_profile)
		page_title = 'Edit Order Information'
		return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def update_settings(request):
	if request.method== 'POST':
		form = UserProfileForm(request.POST)
		if form.is_valid:
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return HttpResponseRedirect('registration/activation_complete.html')
	else:
		if UserProfile(user=request.user):
			current_profile = UserProfile(user=request.user)
			form = UserProfileForm(instance=current_profile)
		return render_to_response('registration/update_settings.html', locals(), context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return render_to_response("registration/logged_out.html", locals())

def my_listed_items(request):
	items_selling = Item.objects.filter(user=request.user)
	return render_to_response('my_listed_items.html', locals(), context_instance=RequestContext(request))
	