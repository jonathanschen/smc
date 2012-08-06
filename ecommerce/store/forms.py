from django import forms
from ecommerce.store.models import Item

class ItemAdminForm(forms.ModelForm):
	class Meta:
		model = Item
	
	def clean_price(self):
		if self.cleaned_data['price'] <= 0:
			raise forms.ValidationError('Price must be greater than zero')
		return self.cleaned_data['price']