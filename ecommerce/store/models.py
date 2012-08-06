from django.db import models
from django.core.mail import send_mail
from django import forms
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=75)
	slug = models.SlugField(max_length=75, unique=True)
	is_active = models.BooleanField(default=True)
	
	class Meta:
		db_table= 'categories'
		verbose_name_plural = 'Categories'
	def __unicode__(self):
		return self.name
	
	@models.permalink
	def get_absolute_url(self):
		return ("ecommerce.store.views.show_category",[str(self.slug)])
		

class Item(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=75)
	slug = models.SlugField(max_length=50, unique=True)
	is_active = models.BooleanField(default=True)
	image =  models.FileField(upload_to="images/")
	price = models.DecimalField(max_digits=9, decimal_places=2)
	quantity = models.IntegerField(default=1)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	shipping_price = models.DecimalField(decimal_places=2, max_digits=6)
	categories = models.ManyToManyField(Category)
	
	class Meta:
		db_table = 'items'
		ordering = ['-created']
	
	def __unicode__(self):
		return self.name
	
	@models.permalink
	def get_absolute_url(self):
		return("ecommerce.store.views.show_item",[str(self.slug)])


class User(models.Model):
	paypal_email = models.EmailField(max_length=75)
	photo = models.FileField(upload_to="images/")
	
	def __unicode__(self):
		return self.username
	 