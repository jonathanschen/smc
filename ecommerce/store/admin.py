from django.contrib import admin
from ecommerce.store.models import *
from ecommerce.store.forms import ItemAdminForm
from ecommerce.accounts.models import UserProfile
from ecommerce.accounts.forms import UserProfileForm
from ecommerce.accounts.models import *


class ItemAdmin(admin.ModelAdmin):
	form = ItemAdminForm
	
	list_display = ('name', 'user', 'price', 'created',)
	list_display_links = ('name',)
	list_per_page = 100
	ordering = ['-created']
	search_fields = ['name', 'description']
	
	prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Item, ItemAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_display_links = ('name',)
	list_per_page = 100
	ordering = ['name']
	search_fields = ['name']
	
	prepopulated_fields = {'slug': ('name',)}
	
admin.site.register(Category, CategoryAdmin)

class UserProfileAdmin(admin.ModelAdmin):
	form = UserProfileForm

admin.site.register(UserProfile, UserProfileAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('lastname',)
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('order', 'item', 'price', 'quantity',)
admin.site.register(OrderItem, OrderItemAdmin)

	