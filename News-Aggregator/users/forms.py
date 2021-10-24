from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import GENDER_OPTIONS, INTEREST_CHOICES, Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	
	gender = forms.ChoiceField(choices=GENDER_OPTIONS,widget=forms.RadioSelect,initial='male')
	mobile = forms.IntegerField()
	address = forms.CharField()
	interest = forms.MultipleChoiceField(
		choices = INTEREST_CHOICES,
		initial = 'top',
		widget = forms.CheckboxSelectMultiple,
        help_text = "<strong>Note:</strong> Select the checkboxes to read news of your Interest",
	)

	class Meta:
		model = User
		fields = ('username', 'first_name','last_name','email', 'password1', 'password2','gender','mobile','address','interest')

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['gender','mobile','address','interest','image']