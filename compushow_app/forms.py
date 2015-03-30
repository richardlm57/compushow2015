from django import forms
from django.core.validators import RegexValidator

# Form para la creación de un estacionamiento

class LoginForm(forms.Form):
	carnet_validator = RegexValidator(
                            regex = '^\d{2}-\d{5}$',
                            message = 'Debes introducir un formato válido.'
                        )
	Carnet = forms.CharField(max_length = 8,required = True, validators = [carnet_validator])
	Password = forms.CharField(widget=forms.PasswordInput())
