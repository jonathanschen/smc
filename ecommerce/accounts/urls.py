from django.conf.urls.defaults import *
from ecommerce import settings
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import password_reset, password_reset_done, password_change, password_change_done

urlpatterns = patterns('ecommerce.accounts.views', 

	url(r'^my_account/$', 'my_account', {'template_name': 'registration/my_account.html'}, 'my_account'),
	url(r'^order_details/(?P<order_id>[-\w]+)/$', 'order_details', {'template_name': 'registration/order_details.html'}, 'order_details'),
	url(r'^order_info/$', 'order_info', {'template_name': 'registration/order_info.html'}, 'order_info'),
	url(r'^my_account/update_settings/$', 'update_settings'),
	url(r'^profile/$', direct_to_template, {'template': 'registration/profile.html'}),
	url(r'^password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'}),
	url(r'^password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}),
	url(r'^password_change/$', password_change, {'template_name': 'registration/password_change_form.html'}),
	url(r'^password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
	url(r'^logout/$', 'logout_view'),
	url(r'^my_listed_items/$', 'my_listed_items'),
)
urlpatterns += patterns('django.contrib.auth.views',
	url(r'^login/$', 'login', {'template_name': 'registration/login.html'}, 'login'), 
)

