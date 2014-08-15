from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CDA',
        'USER': 'cintia',
        'PASSWORD': 'pass', 
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '793266537373794' 
SOCIAL_AUTH_FACEBOOK_SECRET = 'b57673eacaaebb222f7ece9484e76823'

SOCIAL_AUTH_TWITTER_KEY = 'xS51ooi7nwTqlLn6BXPSCSFUA'  
SOCIAL_AUTH_TWITTER_SECRET = 'dK822abV1mPOlBXeLPEMyF9CumB0kgWkOOxGYXNQobftdZM1bb'

MANDRILL_API_KEY = 'HMGKvzYz5AEqfrvGxdgh3A'
