from django import forms
from ecommerce.store.models import Item


class ItemAdminForm(forms.ModelForm):
	class Meta:
		model = Item
	
	def clean_price(self):
		if self.cleaned_data['price'] <= 0:
			raise forms.ValidationError('Price must be greater than zero')
		return self.cleaned_data['price']

class ItemAddToCartForm(forms.Form):
	quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2',
	'value':'1', 'class':'quantity', 'maxlength':'5'}),
	error_messages={'invalid':'Please enter a valid quantity.'}, min_value=1)
	
	item_slug = forms.CharField(widget=forms.HiddenInput())
	
	def __init__(self, request=None, *args, **kwargs):
		self.request = request
		super(ItemAddToCartForm, self).__init__(*args, **kwargs)
	
	def clean(self):
		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError("Cookies must be enabled")
		return self.cleaned_data
		
class AddItem(forms.ModelForm):
	name = forms.CharField(label="Title")
	
	
	class Meta:
		model = Item
		exclude = ('user','slug','is_active',)

class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	message = forms.CharField()
	email = forms.EmailField()
