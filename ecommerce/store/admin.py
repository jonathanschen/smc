from django.contrib import admin
from ecommerce.store.models import *
from ecommerce.store.forms import ItemAdminForm

class ItemAdmin(admin.ModelAdmin):
	form = ItemAdminForm
	
	list_display = ('name', 'price','created',)
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
	