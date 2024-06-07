from pathlib import Path
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# Configuración de reCAPTCHA
RECAPTCHA_PUBLIC_KEY = 'TU_CLAVE_DE_SITIO'
RECAPTCHA_PRIVATE_KEY = 'TU_CLAVE_SECRETA'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['172.16.1.20',
                 '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogos',
    'sesions',
    'armamento',
    'imagenes',
    'utilidades',
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

ROOT_URLCONF = 'rnae.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rnae.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': dj_database_url.config(
    #     default='postgresql://postgres:postgres@localhost:5432/rnae',
    #     conn_max_age=600
    # )
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rnae_bus',
        'USER': 'admin_rnae',
        'PASSWORD': 'rnae_admin',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Mexico_City'
DATE_FORMAT = 'j \de F \de Y'

USE_i18N = True
USE_TZ = True
USE_L10N = True

LANGUAGES = [
    ('en', 'Ingles'),
    ('es', 'Español'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),  # Carpeta donde se guardarán los archivos de traducción
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'home/sistemas/RNAE/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    # Otras rutas de archivos estáticos si las tienes
]

LOGIN_URL = '/iniciar_sesion'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ruta donde se almacenarán los archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL base para servir archivos multimedia
MEDIA_URL = '/media/'

IMAGES_ROOT = os.path.join(MEDIA_ROOT, 'images')

IMAGENES_ROOT = os.path.join(IMAGES_ROOT, 'Imagenes')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

