import environ

from api.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG",False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": {        
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'listafacil',
        'USER': 'listafacil',
        'PASSWORD': 'p73W54ARuE8oM6oi',
        'HOST': '144.91.110.253',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        }
}