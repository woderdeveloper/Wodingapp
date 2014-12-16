"""Production settings and globals."""
from os import environ
from base import *

########## EMAIL CONFIGURATION
EMAIL_HOST      = 'mywoding.com'
EMAIL_HOST_PASSWORD = 'Woding@2014'
EMAIL_HOST_USER = 'mywoding'
EMAIL_PORT      = 26
EMAIL_USE_TLS   = False
DEFAULT_FROM_EMAIL  = 'info@mywoding.com'
SERVER_EMAIL = 'django@my-domain.com'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mywoding_app',                      # Or path to database file if using sqlite3.
        'USER': 'mywoding_app',                      # Not used with sqlite3.
        'PASSWORD': 'Woding@2014',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }

}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
#CACHES = memcacheify()
########## END CACHE CONFIGURATION


########## CELERY CONFIGURATION
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-transport
BROKER_TRANSPORT = 'amqplib'

# Set this number to the amount of allowed concurrent connections on your AMQP
# provider, divided by the amount of active workers you have.
#
# For example, if you have the 'Little Lemur' CloudAMQP plan (their free tier),
# they allow 3 concurrent connections. So if you run a single worker, you'd
# want this number to be 3. If you had 3 workers running, you'd lower this
# number to 1, since 3 workers each maintaining one open connection = 3
# connections total.
#
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-pool-limit
BROKER_POOL_LIMIT = 3

# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-connection-max-retries
BROKER_CONNECTION_MAX_RETRIES = 0

# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-url
BROKER_URL = environ.get('RABBITMQ_URL') or environ.get('CLOUDAMQP_URL')

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'amqp'
########## END CELERY CONFIGURATION



########## COMPRESSION CONFIGURATION
# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
#COMPRESS_STORAGE = DEFAULT_FILE_STORAGE

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
# COMPRESS_CSS_FILTERS += [
#     'compressor.filters.cssmin.CSSMinFilter',
# ]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_JS_FILTERS += [
    'compressor.filters.jsmin.JSMinFilter',
]
COMPRESS_CSS_FILTERS = [
    #creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    #css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]
########## END COMPRESSION CONFIGURATION


########## END SECRET CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']
########## END ALLOWED HOST CONFIGURATION

