from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class UserCreationForm(UserCreationForm):
    captcha = CaptchaField()

