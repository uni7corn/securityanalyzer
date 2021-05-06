"""
Django settings for securityanalyzer project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jy4kb(u3&sjcirx)(mao!6qxzkq$a5&20x%49og&(3_188lp)r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'DynamicAnalyzer.apps.DynamicanalyzerConfig',
    'StaticAnalyzer.apps.StaticanalyzerConfig',
    'Home.apps.HomeConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'securityanalyzer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'securityanalyzer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_URL = '/static/'

# STATIC_ROOT = BASE_DIR/'static'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# ===========================================CONFIG===========================================
# =============ALLOWED DOWNLOAD EXTENSIONS=====
ALLOWED_EXTENSIONS = {
    '.txt': 'text/plain',
    '.png': 'image/png',
    '.zip': 'application/zip',
    '.tar': 'application/x-tar',
    '.apk': 'application/octet-stream',
}
# =============ALLOWED MIMETYPES=================

APK_MIME = [
    'application/octet-stream',
    'application/vnd.android.package-archive',
    'application/x-zip-compressed',
    'binary/octet-stream',
]

ZIP_MIME = [
    'application/zip',
    'application/octet-stream',
    'application/x-zip-compressed',
    'binary/octet-stream',
]
# =======ANDROID DYNAMIC ANALYSIS SETTINGS===========
ANALYZER_IDENTIFIER = ''
FRIDA_TIMEOUT = 4

# ================HTTPS PROXY ===============
PROXY_IP = '192.168.31.14'
PROXY_PORT = 4272  # Proxy Port

# ========UPSTREAM PROXY SETTINGS ==============
# If you are behind a Proxy
UPSTREAM_PROXY_ENABLED = False
UPSTREAM_PROXY_SSL_VERIFY = True
UPSTREAM_PROXY_TYPE = 'http'
UPSTREAM_PROXY_IP = '127.0.0.1'
UPSTREAM_PROXY_PORT = 3128
UPSTREAM_PROXY_USERNAME = ''
UPSTREAM_PROXY_PASSWORD = ''

# =============Download Directory================
DWD_DIR = MEDIA_ROOT / 'downloads/'
FRIDA_SERVER = 'https://api.github.com/repos/frida/frida/releases/tags/'

TOOLS_DIR = BASE_DIR / 'DynamicAnalyzer/tools/'
# Screenshot Directory
SCREEN_DIR = MEDIA_ROOT / 'downloads/screen/'
JAVA_DIRECTORY = ''
ADB_BINARY = ''
SCALA_DIRECTORY = ''
# ==========ANDROID SKIP CLASSES==========================
# Common third party classes/paths that will be skipped
# during static analysis
SKIP_CLASS_PATH = {
        'com/google/', 'androidx', 'okhttp2/', 'okhttp3/',
        'com/android/', 'com/squareup', 'okhttp/'
        'android/content/', 'com/twitter/', 'twitter4j/',
        'android/support/', 'org/apache/', 'oauth/signpost',
        'android/arch', 'org/chromium/', 'com/facebook',
        'org/spongycastle', 'org/bouncycastle',
        'com/amazon/identity/', 'io/fabric/sdk',
        'com/instabug', 'com/crashlytics/android',
    }
# Better logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s] %(asctime)-15s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'color': {
            '()': 'colorlog.ColoredFormatter',
            'format':
                '%(log_color)s[%(levelname)s] %(asctime)-15s : %(pathname)s --> %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'log_colors': {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR/'logs'/'debug.log',
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color',
        },
    },
    'loggers': {
        # 'django': {
        #     'handlers': ['console', 'logfile'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'django.db.backends': {
        #     'handlers': ['console', 'logfile'],
        #     # DEBUG will log all queries, so change it to WARNING.
        #     'level': 'INFO',
        #     'propagate': False,   # Don't propagate to other handlers
        # },
        'securityanalyzer': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'StaticAnalyzer': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'DynamicAnalyzer': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'Home': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}