from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils import translation
from django.conf import settings
# Create your views here.
def registrarse(request):
    if request.method == 'GET':
        print('enviando formulario')
        return render(request, 'sign_up.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                
                user.save()
                login(request, user)
                return redirect('catalogos')
            except IntegrityError:
                return render(request, 'sign_up.html',{
                'form': UserCreationForm,
                'error': 'User already exists'
                })
        return render(request, 'sign_up.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })
  
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'sign_in.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sign_in.html',{
            'form': AuthenticationForm,
            'error': 'Usuario o Contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')  

def cambiar_lenguaje(request, language_code):
    if language_code in dict(settings.LANGUAGES):
        print(request.session['django_language'])
        request.session['django_language'] = language_code
        translation.activate(language_code)
        print(request.session['django_language'])
    else:
        print("error")
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer)