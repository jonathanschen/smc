from django.shortcuts import render_to_response 
from django.template import RequestContext, Context
from ecommerce.cart import cart
from paypal.standard.forms import PayPalPaymentsForm
from paypal.pro.views import PayPalPro
from ecommerce import settings

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
	item = {
	"amt": "10.00", # amount to charge for item
	"inv": "inventory", # unique tracking variable paypal
	'currencycode': 'USD',
	'shiptoname' : 'John Smith',
	'shiptostreet' : 'Street 1',
	'shiptostreet_2' : 'Street 2',
	'landingpage' : 'Billing',
	'shippingamt' : 0,
	'shiptocity' : 'Las Vegas',
	'shiptostate' : 'Nevada',
	'shiptocountrycode' : 'US',
	'shiptozip' : '27705', # is country
	'shiptophonenum' : "666-666-5948",
	'addroverride' : "1",
	'email' : 'john@smith.com',
	# "noshipping" : "0",
	"custom": '555', # custom tracking variable for you
	# of course in this case URL is your webpage URL
	"cancelurl": settings.URL + "error", # error page
	"returnurl": settings.URL + "success"} # success page
#	amount = 2
	# your items
#	item["l_name0" ] = "Extra product #1"
#	item["l_amt0"] = 25
#	item["l_qty0"] = 1
#	item["l_name1" ] = "Extra product #2"
#	item["l_amt1"] = 25
#	item["l_qty1"] = 1
	# rewrite about
#	item['amt'] = 2
	
	kw = {"item": item, # what you're selling
	"success_url": "/success/"} # redirect location after success, I am not sure but it shouldn't work
	ppp = PayPalPro(**kw)
	return ppp(request)