from wishlist.settings.base import *

SECRET_KEY = 'c0eio4ik-#$alyutl^s(1y@g&fy@+$4(+*heum*n4=sr8j)x9h'
DEBUG = True
ALLOWED_HOSTS = []

# Meta settings.
META_SITE_PROTOCOL = 'http'
META_SITE_DOMAIN = 'localhost:8888'
META_USE_OG_PROPERTIES = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meadowspto',
        'USER': 'meadowspto',
        'PASSWORD': 'meadowspto',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Site settings.
GOOGLE_ANALYTICS_ID = ''