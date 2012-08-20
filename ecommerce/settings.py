import dj_database_url
import os

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8'))
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAIHY3KM3YKXYQ3IUQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'taidai'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AUTH_PROFILE_MODULE = 'accounts.UserProfile'
DEBUG = True
THUMBNAIL_DEBUG = True
TEMPLATE_DEBUG = DEBUG
URL = 'http://blooming-depths-4028.herokuapp.com/'
ADMINS = (
    # ('Jonathan Chen', 'jonathanschen@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'awa',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#DATABASES = {
#    'default': dj_database_url.config(default='postgres://localhost')
#}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(CURRENT_PATH, 'ecommerce', 'store', 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'https://s3.amazonaws.com/taidai/'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/Users/jonathanschen/Python/projects/skeleton/ecommerce/ecommerce/store/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'https://s3.amazonaws.com/taidai'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#5qmy-@lbk7j9et+mzp%8=zf)akmhl%5%d9e-#0zx+m&amp;&amp;s6o51'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ecommerce.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ecommerce.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(CURRENT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecommerce.store',
	'ecommerce.accounts',
	'ecommerce.cart',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
	'registration',
	'sorl.thumbnail',
	'paypal.standard',
	'paypal.pro',
	'storages',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
DISQUS_API_KEY = 'dW5RaIZ0T8po4YTAOp94DVjiQoI5fai7aHWmfiroCAbNcydiZg9BfqYlP2UWtjCH'
DISQUS_WEBSITE_SHORTNAME = 'taidai'
PAYPAL_RECEIVER_EMAIL = 'jsc37_1345062968_biz@gmail.com'
PAYPAL_TEST = False
PAYPAL_WPP_USER = 'jsc37_1345062968_biz_api1.gmail.com'
PAYPAL_WPP_PASSWORD = '1345062991'
PAYPAL_WPP_SIGNATURE = 'ALBsd9K1rmWR.udv3uRzD1e0fV6RAY6cC7rjgrI9zyC9wJQSPeLu4cV5'
LOGIN_REDIRECT_URL = '../my_account/'
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ldb102082@gmail.com'
EMAIL_HOST_PASSWORD = '@Pingan82'
EMAIL_PORT = 587
