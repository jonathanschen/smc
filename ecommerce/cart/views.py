from django.shortcuts import render_to_response 
from django.template import RequestContext, Context
from ecommerce.cart import cart
from paypal.standard.forms import PayPalPaymentsForm
from paypal.pro.views import PayPalPro
from paypal.pro.forms import PaymentForm
from ecommerce import settings
from ecommerce.accounts.models import OrderItem
import decimal


def show_cart(request, template_name="cart/cart.html"): 
	if request.method == 'POST':
		postdata = request.POST.copy()
		if postdata['submit'] == 'Remove':
			cart.remove_from_cart(request)
		if postdata['submit'] == 'Update':
			cart.update_cart(request)
	cart_items = cart.get_cart_items(request)
	page_title = 'Shopping Cart'
	cart_subtotal = cart.cart_subtotal(request)
	return render_to_response(template_name, locals(), 
	context_instance=RequestContext(request))



def express_payment(request):
	user = request.user
	cart_subtotal = cart.cart_subtotal(request)
	
	if request.method == "POST":
		form = PaymentForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			order.buyer = request.user
			order.transaction_id = order
			order.save()
			if order.pk:
				cart_items = cart.get_cart_items(request)
				for item in cart_items:
					order_item = OrderItem(item=item.item_id, quantity=item.quantity, price=item.item_id.price, order=order)
					order_item.save()
	item = {
	"amt": cart_subtotal, # amount to charge for item
	"invnum": "696969696", # unique tracking variable paypal
	"custom": '555', # custom tracking variable for you
	"cancelurl": settings.URL + "error", # error page
	"returnurl": settings.URL + "success"} # success page
		
	kw = {"item": item, # what you're selling
	"success_url": "/success/"} # redirect location after success, I am not sure but it shouldn't work
	ppp = PayPalPro(**kw)
	return ppp(request)