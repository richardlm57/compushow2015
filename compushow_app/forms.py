from django import forms
from django.core.validators import RegexValidator
from compushow_app.models import Foto

# Form para la creación de un estacionamiento

class Login_Signup_Form(forms.Form):
    carnet_validator = RegexValidator(
                            regex = '^\d{2}-\d{5}$',
                            message = 'Debes introducir un formato válido.'
                        )
    Carnet = forms.CharField(max_length=8,
                             required=True,
                             validators=[carnet_validator])
    Password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
    Computista = forms.CharField(max_length=70)
    Password   = forms.CharField(widget=forms.PasswordInput())
    Cpassword  = forms.CharField(widget=forms.PasswordInput())

class NominacionForm(forms.Form):
    nominado = forms.CharField(max_length=70)

class FotoForm(form.ModelForm):

    class Meta:
        model = Foto