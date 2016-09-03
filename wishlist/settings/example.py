from wishlist.settings.base import *

SECRET_KEY = 'A_SECRET_KEY'
DEBUG = True
ALLOWED_HOSTS = []

# Meta settings.
META_SITE_PROTOCOL = 'http'
META_SITE_DOMAIN = 'localhost:8888'
META_USE_OG_PROPERTIES = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wishlist',
        'USER': 'wishlist',
        'PASSWORD': 'wishlist',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Accounts.
GOOGLE_ANALYTICS_ID = ''
AMAZON_ACCESS_KEY = ''
AMAZON_SECRET_KEY = ''
AMAZON_ASSOC_TAG = ''