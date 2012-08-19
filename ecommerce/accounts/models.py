from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField
from django.forms import ModelForm
from django import forms
from ecommerce.store.models import Item
from paypal.pro.fields import CreditCardField, CreditCardExpiryField, CreditCardCVV2Field, CountryField
import decimal

class UserProfile(models.Model):
	
	user = models.OneToOneField(User)
	activation_key = models.CharField(max_length=40, blank=True)
	first_name = models.CharField(max_length=50, blank=True)
	last_name = models.CharField(max_length=50, blank=True)
	phone_number = PhoneNumberField(blank=True, null=True)
	address_line_1 = models.CharField(max_length=300, blank=True)
	address_line_2 = models.CharField(max_length=300, blank=True)
	address_line_3 = models.CharField(max_length=300, blank=True)
	city = models.CharField(max_length=150, blank=True)
	postalcode = models.CharField(max_length=10, blank=True)
	paypal_email = models.EmailField(max_length=75, blank=True)
	photo = models.ImageField(upload_to="images/", blank=True)

	
	#def create_user_profile(sender, instance, created, **kwargs):
	#	if created:
	#		Customer.objects.create(user=instance)
	#post_save.connect(create_user_profile, sender=User)

	
	def __unicode__(self):
		return self.user.username
		
	def save(self, *args, **kwargs):
		try:
			existing = UserProfile.objects.get(user=self.user)
			self.id = existing.id #force update instead of insert
		except UserProfile.DoesNotExist:
			pass 
		models.Model.save(self, *args, **kwargs)



class Order(models.Model):

	date = models.DateTimeField(auto_now_add=True)
	buyer = models.ForeignKey(User, related_name="buyer")
	transaction_id = models.CharField(max_length=20)
	
	email = models.EmailField(max_length=50, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	
	shipping_firstname = models.CharField("First Name", max_length=50)
	shpping_lastname = models.CharField("Last Name", max_length=50)
	shipping_address_1 = models.CharField(max_length=50)
	shipping_address_2 = models.CharField(max_length=50)
	shipping_city = models.CharField(max_length=50)
	shipping_state = models.CharField(max_length=2)
	shipping_zip = models.CharField(max_length=10)

	
	firstname = models.CharField("Billing First Name", max_length=50)
	lastname = models.CharField("Billing Last Name", max_length=50)
	street = models.CharField(max_length=50) 
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	zip = models.CharField(max_length=10)

	
	def __unicode__(self):
		return 'Order #' + str(self.id)
	
	@property	
	def total(self):
		total = decimal.Decimal('0.00')
		order_items = OrderItem.objects.filter(order=self)
		for item in order_items:
			total += item.total
		return total

class OrderItem(models.Model):
	item = models.ForeignKey(Item)
	quantity = models.IntegerField(default=1)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	order = models.ForeignKey(Order)
	
	@property
	def total(self):
		return self.quantity * self.price
	
	@property
	def name(self):
		return self.item.name
	
	def __unicode__(self):
		return self.item.name
	
	def get_absolute_url(self):
		return self.item.get_absolute_url()