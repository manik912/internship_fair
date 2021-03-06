from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User

class UserRegistrationForm(UserCreationForm):
	email 				= forms.EmailField(help_text='Email Id used for registration cannot be changed later.')
	name 				= forms.CharField(max_length=60)
	contact 			= PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"), required=False, help_text='Add Country Code before your contact number.') 
	

	class Meta(UserCreationForm.Meta):
		model 	= User
		fields 	= ['name', 'email', 'contact', 'password1', 'password2']
	
	@transaction.atomic
	def clean(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Account with this email already exists")
		return self.cleaned_data

