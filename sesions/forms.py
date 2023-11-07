from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from captcha.fields import CaptchaField

class UserCreationForm(UserCreationForm):
    captcha = CaptchaField()

class AuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()
