# prod.py for your server Django settings
from test_tuning.settings.common import *

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "hyperbolagaming"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

DATABASES = {    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydbname',
        'USER' : 'futouyiba',
        'PASSWORD' : 'bxy1367894',
        'HOST' : 'hyperbolagaming.cfuzg7xb2jfr.us-west-2.rds.amazonaws.com',
        'PORT' : '5432',
    }
}