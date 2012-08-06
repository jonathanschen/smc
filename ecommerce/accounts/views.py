from django.contrib.auth forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpReponseRedirect
#from ecommerce.checkout.models iport Order, OrderItem
from django.contrib.auth.decorators import login_required

def register(request, template_name="registration/register.html"):
	if request.method == "POST":
		postdata = request.POST.copy()
		form = UserCreationForm(postdata)
		if form.is_valid():
			form.save()
			un = postdata.get('username','')
			pw = postdata.get('password1','')
			from django.contrib.auth import login, authenticate
			new_user = authenticate(username=un, password=pw)
			if new_user and new_user.is_active:
				login(request, new_user)
				url = urlresolvers.reverse('my_account')
				return HttpResponseRedirect(url)
			else:
				form = UserCreationForm()
			page_title = 'UserRegistration'
			return render_to_response(template_name, locals(), context_instance=RequestContext(request))
def my_account:
def order_details:
def order_info: