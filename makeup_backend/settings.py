"""
Django settings for makeup_backend project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from os import getenv
import os
import django_heroku
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# Add .env variables anywhere before SECRET_KEY
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['SECRET_KEY']

SECRET_KEY = str(os.getenv('SECRET_KEY'))




# load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("IS_DEVELOPMENT", True)

ALLOWED_HOSTS = [
    #  'django-env.eba-xmmvkvyn.us-east-1.elasticbeanstalk.com'
    # makeup-env.eba-2sm3qfyw.us-east-2.elasticbeanstalk.com/
    
]


AUTHENTICATION_BACKENDS = [
  'django.contrib.auth.backends.ModelBackend',
  'guardian.backends.ObjectPermissionBackend',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'makeup.apps.MakeupConfig',
    # 'makeup',
    'crispy_forms',
    'guardian',
    'corsheaders',
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASS' : [
        'rest_framework.permission.IsAuthenticatedOrReadOnly',

    ]
}


CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]

CRISPY_TEMPLATE_PACK = 'uni_form'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',


    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'makeup_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
                
            ],
        },
    },
]

WSGI_APPLICATION = 'makeup_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'makeup',
#         'HOST': 'localhost',
#         'PORT': '5432',
#         'USER': 'anfalfadhil',
#         'PASSWORD' : 'Sa1865969$$'
#     }
# }


ALLOWED_HOSTS=['makeup-backend.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd58s6cqbcpo0ve',
        'HOST': 'ec2-3-230-122-20.compute-1.amazonaws.com',
        'PORT': '5432',
        'USER': 'qfybhhjofoqves',
        'PASSWORD' : '33ab4541043592b48c41760f92367309077ba6e7425ceef266c6cbbcd9dcdda1'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = '/static/'



# CORS_ALLOW-ALL-ORIGINS = True




STATICFILES_DIRS = [
    BASE_DIR / "makeup/static"
]

MEDIA_ROOT = BASE_DIR / "blog_images"
MEDIA_URL = "/docs/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK='bootstrap4'
