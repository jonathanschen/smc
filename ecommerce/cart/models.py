from django.db import models
from ecommerce.store.models import *

class Cart(models.Model):
	cart_id = models.CharField(max_length=50)
	item_id = models.ForeignKey('store.Item', unique=False)
	date_added = models.DateTimeField(auto_now_add=True)
	quantity = models.IntegerField(default=1)
	
	class Meta:
		db_table = 'cart_items'
		ordering = ['date_added']
	
	def total(self):
		return self.quantity * self.item_id.price
	
	def name(self):
		return self.item_id.name
	
	def price(self):
		return self.item_id.price
	
	def get_absolute_url(self):
		return self.item_id.get_absolute_url()
	
	def augment_quantity(self, quantity):
		self.quantity = self.quantity + int(quantity)
		self.save()