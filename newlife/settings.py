"""
Django settings for newlife project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from __future__ import unicode_literals
import environ
ROOT = environ.Path(__file__) - 2
ENV = environ.Env(DEBUG=(bool, False),) # set default values and casting

ENV.read_env(ROOT('.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k88_v(c1@-z9njx696ii(qyo5rh*tblyfzi8qinbmw02^eij97'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV('DEBUG')

ALLOWED_HOSTS = ['newlife.begg.digital']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django.contrib.gis',
    'rest_framework',
    
    'tinymce',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'newlife.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ROOT('templates')],
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

WSGI_APPLICATION = 'newlife.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': ENV.db(default='spatialite:///%s' % ROOT('database.sqlite')),
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ENV('STATIC_ROOT', default=ROOT('static_deploy'))

STATICFILES_DIRS = (
                    ROOT('static'),
                    )

DEFAULT_FROM_EMAIL = 'info@beggdigital.com'
EMAIL_SUBJECT_PREFIX = ENV('EMAIL_PREFIX', default='[newlife Dev]')
SERVER_EMAIL = 'web@beggdigital.com'

CSRF_COOKIE_SECURE = ENV.bool('HTTPS_ONLY', default=False)
SESSION_COOKIE_SECURE = ENV.bool('HTTPS_ONLY', default=False)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')
USE_X_FORWARDED_HOST = False

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ),
    'PAGE_SIZE': 50
}
