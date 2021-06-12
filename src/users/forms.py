from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.formsets import MAX_NUM_FORM_COUNT

class UserRegisterForm(UserCreationForm):
    #username = forms.CharField(max_length=150, label="Nutzername")
    email = forms.EmailField(label="Email-Adresse")
    first_name = forms.CharField(max_length=150, label="Vorname")
    last_name = forms.CharField(max_length=150, label="Nachname")
    # password1 = forms.CharField(max_length=150, label="Passwort")
    # password2 = forms.CharField(max_length=150, label="Passwort wiederholen")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']