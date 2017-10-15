import dj_database_url
import os
from .base import *

DEBUG = os.environ.get('DJANGO_DEBUG', False) == 'True'
ALLOWED_HOSTS = ['*', 'jinyuz-blog.herokuapp.com']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
SECRET_KEY = os.environ.get('SECRET_KEY', 'asdfasdf')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dev.jinyuz@gmail.com'
EMAIL_HOST_PASSWORD = '123523qwe'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
