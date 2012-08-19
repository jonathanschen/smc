from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('ecommerce.store.views',
	url(r'^$', 'index'),
	url(r'^sell/$', 'sell'),
	url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category'),
	url(r'^item/(?P<item_slug>[-\w]+)/$', 'show_item'),
	url(r'^contact/$', 'contact'),
	url(r'^thanks/$', direct_to_template, {'template':'thanks.html'}),
	url(r'^success/$', direct_to_template, {'template':'success.html'}),


)