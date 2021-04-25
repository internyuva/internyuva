"""
Django settings for school project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import json
pas='InternYuvaPA1'
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# with open('/etc/config.json') as config_file:
#     conf = json.load(config_file)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z!bjoc%m(ksd0v68%m(4i#w#_lbr00uq6))w7dg+d^m4#sw0or'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Third Party Apps
    'crispy_forms',
    'embed_video',
    'django_cleanup',


    #s3 bucket
    'storages',

    # 'phonenumber_field',
    # 'phonenumbers',

    #Local Apps
    'accounts',
    'classroom',
    'blog',

    'social_django',
]
AUTH_USER_MODEL = 'accounts.Account'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'school.urls'
# AUTH_USER_MODEL = 'accounts.Account'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'school.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "collectstatic")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
CRISPY_TEMPLATE_PACK='bootstrap4'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                           # 'account.authentication.EmailAuthBackend',
                           'social_core.backends.facebook.FacebookOAuth2',
                           'social_core.backends.google.GoogleOAuth2', 
]


SOCIAL_AUTH_FACEBOOK_KEY = '135176475177358'
SOCIAL_AUTH_FACEBOOK_SECRET = '1fe00f57617b42c46f39e26a62c1096e'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '516902878922-7ka5a33qtpfo0m2h181d2is8tnhmhb0v.apps.googleusercontent.com'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ar0vDZONKmc-PGX-CsdoXHKE'


# samir patil accounts
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '938048506814-h8umhm60uv438465v67450ds7hgoguke.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'LLdmhLTx49Oa6-bTguuxEPRE'






# from .local_settings import *


# AWS_ACCESS_KEY_ID = "AKIAXL4SR7652X5P75AX"
# AWS_SECRET_ACCESS_KEY = "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"
# AWS_STORAGE_BUCKET_NAME = "internyuva"
#
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
#
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='internyuva1@gmail.com'
EMAIL_HOST_PASSWORD=pas
