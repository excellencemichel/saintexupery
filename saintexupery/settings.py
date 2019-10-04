"""
Django settings for saintexupry project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("SECRET_KEY", None)


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ALLOWED_HOSTS = []
BASE_URL ="www.centrecnedsaintexupery.com"





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',

    'crispy_forms',

    'profile',
    'accounts',

    'comments',

    'contacts',

    'cycles',

    'evenements',
    'espaces',

    'fonctionnements',

    'presentation',
    'inscriptions',
    'pdfapp',


]


AUTH_USER_MODEL = "profile.ProfileUser"

FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_END_SESSION = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',



]

ROOT_URLCONF = 'saintexupery.urls'

LOGIN_URL = 'accounts:login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'





TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",

            ],
        },
    },
]

WSGI_APPLICATION = 'saintexupery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2'
    }
}






ADMINS = [ 

        ("Excellence Michel","bnvnmmnl@gmail.com"),
]


MANAGERS = ADMINS



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

CRISPY_TEMPLATE_PACK = "bootstrap4"
STATIC_URL = '/static/'








from .production import *

if os.environ.get("ENV") =="PRODUCTION":
    DEBUG = False
    from saintexupery.aws.conf import *


