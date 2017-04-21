import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'msfh2wr3z9wlzy!kqwg6x##z^+0(xl=3g^4uzh5ldc0pi6b70v'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'pidgeonApi.sms'
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'unslashed.middleware.RemoveSlashMiddleware'
)

ROOT_URLCONF = 'pidgeonApi.urls'

TEMPLATES = []

WSGI_APPLICATION = 'pidgeonApi.wsgi.application'

DATABASES = {}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = False
REMOVE_SLASH = True

STATIC_URL = '/static/'
