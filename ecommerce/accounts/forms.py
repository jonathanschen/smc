from django import forms
from ecommerce.accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(forms.ModelForm):
	
	class Meta:
		model = UserProfile
		exclude = ('user', 'activation_key',)
		
	
	