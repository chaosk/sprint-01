# pylint: disable-all
"""
settings_default.py

Do NOT (!!!) edit this file!
Please override settings in settings_local.py instead.
"""

import os
# Django settings for teerace project.

PROJECT_DIR = os.path.dirname(__file__)

DEBUG = False
TEMPLATE_DEBUG = False
TEMPLATE_CACHING = True

INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
#	('John Doe', 'joe@doe.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'.
		'ENGINE': 'django.db.backends.sqlite3',
		# Or path to database file if using sqlite3.
		'NAME': PROJECT_DIR + '/sprint-01.sqlite',
		# Not used with sqlite3.
		'USER': '',
		# Not used with sqlite3.
		'PASSWORD': '',
		# Set to empty string for localhost. Not used with sqlite3.
		'HOST': '',
		# Set to empty string for default. Not used with sqlite3.
		'PORT': '',
	}
}

# New CACHES setting. Waiting for johnny-cache.
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
	}
}

# Paginator
PAGINATION_DEFAULT_PAGINATION = 20
# ... 2 3 4 [5] 6 7 8 ...
PAGINATION_DEFAULT_WINDOW = 3
# If the last page has 1 object, the object gets attached to previous one instead.
PAGINATION_DEFAULT_ORPHANS = 1
PAGINATION_INVALID_PAGE_RAISES_404 = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory that holds static files.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(MEDIA_ROOT, 'static')

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/media/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'foobar'


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# User profile model
AUTH_PROFILE_MODULE = 'accounts.UserProfile'

# Message storage backend
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'

ABSOLUTE_URL_OVERRIDES = {
	'auth.user': lambda u: "/profile/%s/" % u.id,
}

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	'django.template.loaders.eggs.Loader',
)

if TEMPLATE_CACHING:
	TEMPLATE_LOADERS = (
		('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
	)

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.transaction.TransactionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.request',
	'lib.context_processors.settings',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_DIR, 'templates'),
	os.path.join(PROJECT_DIR, 'templates/piston'),
)

OUR_APPS = (
	'accounts',
	'api',
	'tasks',
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.markup',
	'django.contrib.humanize',
	'lib',
	'south',
) + OUR_APPS

TEST_RUNNER = 'local_tests.LocalTestSuiteRunner'
