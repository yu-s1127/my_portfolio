# import environ
# import os
# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# # BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# env = environ.Env()

# HEROKU_ENV = env.bool('DJANGO_HEROKU_ENV', default=False)
# if not HEROKU_ENV:
#     env.read_env('.env')

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# DEBUG = env.bool('DEBUG', False)

# SECRET_KEY = env('SECRET_KEY')

# ALLOWED_HOSTS = ['127.0.0.1', 'yuhei-portfolio.herokuapp.com']


# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'widget_tweaks',
#     'app.apps.AppConfig',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'my_portfolio.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'my_portfolio.wsgi.application'

# # Database
# # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
# #     }
# # }

# try:
#     from .local_settings import *
# except ImportError:
#     pass

# # Password validation
# # https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# LOGGING = {
#     'formatters': {
#         'verbose': {
#             'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
#                        'pathname=%(pathname)s lineno=%(lineno)s '
#                        'funcname=%(funcName)s %(message)s'),
#             'datefmt': '%Y-%m-%d %H:%M:%S'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         }
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     }
# }


# # Internationalization
# # https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'ja'

# TIME_ZONE = 'Asia/Tokyo'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIR = os.path.join(BASE_DIR, 'staticfiles')


# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_PORT = env('EMAIL_PORT')
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = env('EMAIL_USE_TLS')

# if not DEBUG:
#     import django_heroku
#     django_heroku.settings(locals())
#     SECURE_SSL_REDIRECT = True
# STATICFILES_STORSGE =
# 'whitenoise.storage.CompressedManifest.FilesStorage'


import os
import environ
import django_heroku
import dj_database_url

env = environ.Env()

HEROKU_ENV = env.bool('DJANGO_HEROKU_ENV', default=False)
if not HEROKU_ENV:
    env.read_env('.env')


DEBUG = env.bool('DEBUG', False)

CLOUD = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'yuhei-portfolio.herokuapp.com',
    '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'app.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_portfolio.wsgi.application'

try:
    from .local_settings import *
except ImportError:
    pass

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')


if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())
