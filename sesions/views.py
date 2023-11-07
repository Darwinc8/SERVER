from django.shortcuts import render, redirect
from .forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils.translation import activate
from django.conf import settings
# Create your views here.
def registrarse(request):
    if request.method == 'GET':
        print('enviando formulario')
        form = UserCreationForm()
        return render(request, 'sign_up.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                if form.cleaned_data['captcha']:
                    try:
                        user = User.objects.create_user(
                            username=request.POST['username'], password=request.POST['password1'])
                        user.is_active = False  # Establecer el usuario como inactivo
                        user.save()
                        login(request, user)
                        return redirect('catalogos')
                    except IntegrityError:
                        return render(request, 'sign_up.html', {
                            'form': form,
                            'error': 'El usuario ya existe'
                        })
                else:
                    return render(request, 'sign_up.html', {
                        'form': form,
                        'error': 'Por favor complete el CAPTCHA'
                    })
            else:
                return render(request, 'sign_up.html', {
                    'form': form,
                    'error': 'La contraseña no coincide'
                })
        else:
            return render(request, 'sign_up.html', {'form': form})
  
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Usuario no encontrado
                return render(request, 'sign_in.html', {'form': form, 'error': 'Usuario no encontrado. Por favor, inténtalo de nuevo.'})
        else:
            # Error de CAPTCHA o cualquier otro error en el formulario
            return render(request, 'sign_in.html', {'form': form})
    else:
        return render(request, 'sign_in.html', {'form': AuthenticationForm()})

@login_required
def cambiar_lenguaje(request, language_code):
    if language_code == "es" or language_code == "en": 
        response = redirect(request.META.get('HTTP_REFERER'))
        activate(language_code)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
        request.session[settings.LANGUAGE_COOKIE_NAME] = language_code
        return response
    else:
        return redirect('home')