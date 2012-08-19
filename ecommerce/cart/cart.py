from ecommerce.cart.models import Cart
from ecommerce.store.models import Item
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import decimal
import random

CART_ID_SESSION_KEY = 'cart_id'

#need this to give each cart a unique id to identify it by
def _cart_id(request):
	if request.session.get(CART_ID_SESSION_KEY,'') == '':
		request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
	return request.session[CART_ID_SESSION_KEY]

#need this to generate that id if the user doesnt have one
def _generate_cart_id():
	cart_id = ''
	characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
	cart_id_length = 50
	for y in range(cart_id_length):
		cart_id += characters[random.randint(0, len(characters)-1)]
	return cart_id

#need this to return a specific Cart based on the id thats posted
def get_cart_items(request):
	return Cart.objects.filter(cart_id=_cart_id(request))
	
def add_to_cart(request):
	postdata = request.POST.copy()
	item_slug = postdata.get('item_slug','')
	quantity = postdata.get('quantity',1)
	item = get_object_or_404(Item, slug=item_slug)
	cart_items = get_cart_items(request)
	item_in_cart = False
	for cart_item in cart_items:
		if cart_item.item_id.id == item.id:
			cart_item.augment_quantity(quantity)
			item_in_cart = True
	if not item_in_cart:
		ci = Cart()
		ci.item_id = item
		ci.quantity = quantity
		ci.cart_id = _cart_id(request)
		ci.save()

def cart_distinct_item_count(request):
	return get_cart_items(request).count()

def get_single_item(request, item_id):
	return get_object_or_404(Cart, id=item_id, cart_id=_cart_id(request))

def update_cart(request):
	postdata = request.POST.copy()
	item_id = postdata['item_id']
	quantity = postdata['quantity']	
	cart_item = get_single_item(request, item_id)
	if cart_item:
		if int(quantity) > 0:
			cart_item.quantity = int(quantity)
			cart_item.save()
		else:
			remove_from_cart(request)

def remove_from_cart(request):
	postdata = request.POST.copy()
	item_id = postdata['item_id']
	cart_item = get_single_item(request, item_id)
	if cart_item:
		cart_item.delete()

def cart_subtotal(request):
	cart_total = decimal.Decimal('0.00')
	cart_items = get_cart_items(request)
	for cart_item in cart_items:
		cart_total += cart_item.item_id.price * cart_item.quantity + cart_item.item_id.shipping_price
	return cart_total

