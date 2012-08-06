from django.conf.urls.defaults import *

urlpatterns = patterns('ecommerce.store.views',
	url(r'^$', 'index'),
	url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category'),
	url(r'^item/(?P<item_slug>[-\w]+)/$', 'show_item'),
)