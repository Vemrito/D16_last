"""
Django settings for NewsPaper project.


For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent





SECRET_KEY = '!4@4-x35lze5&am*fjh)!xo(9##389=)b)$pw14sps_1n)+ja0'


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']




INSTALLED_APPS = [
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',


    'news',


    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',

    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'news.middlewares.TimezoneMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',


    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




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




LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Русский'),
]

TIME_ZONE = 'Europe/Moscow'
#'UTC'


USE_I18N = True

USE_L10N = True

USE_TZ = True





STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATICFILES_DIRS = [
        BASE_DIR / "static",

]


LOGIN_URL = '/accounts/login/'
SITE_ID = 1


LOGIN_REDIRECT_URL = '/'



ADMINS = (
    ('admin', 'oleg_artist@list.ru'),
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_FORMS = {'signup': 'NewsPaper.models.BasicSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'Skill.testing'
EMAIL_HOST_PASSWORD = 'qAzSe$123'
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

DEFAULT_FROM_EMAIL = 'Skill.testing@yandex.ru'
SERVER_EMAIL = 'Skill.testing@yandex.ru'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
        'general': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'errors': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'warning': {
            'format': '%(asctime)s %(pathname)s %(levelname)s %(message)s'
        },

    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
            },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'console': {

            'class': 'logging.StreamHandler',
            'formatter': 'console',

        },
        'mail_admins': {
            'level': 'INFO',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'errors',
        },
        'general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'general',
            'filename': 'general.log',
            'filters': ['require_debug_false'],
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'errors',
            'filename': 'errors.log'
        },
        'security': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'general',
            'filename': 'security.log'
        },
    },
    'loggers': {
        '': {

            'handlers': ['console'],
            'propagate': True
        },
        'NewsPaper': {
            'level': 'INFO',
            'handlers': ['general'],
            'propagate': True
         },
        'news': {
            'level': 'INFO',
            'handlers': ['general'],
            'propagate': True
         },
        'django': {
            'level': 'INFO',
            'handlers': ['general'],
            'propagate': True
         },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['errors', 'mail_admins'],
            'propagate': True
        },
        'django.server': {
            'level': 'ERROR',
            'handlers': ['errors', 'mail_admins'],
            'propagate': True
        },
        'django.template': {
            'level': 'ERROR',
            'handlers': ['errors'],
            'propagate': True
        },
        'django.db_backends': {
            'level': 'ERROR',
            'handlers': ['errors'],
            'propagate': True
        },
        'django.security': {
            'level': 'ERROR',
            'handlers': ['security'],
            'propagate': True
        },
    }
}

LOCALE_PATH = [
    os.path.join(BASE_DIR, 'locale')
]

