from pathlib import Path

from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_template.urls'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ]
        ,
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

WSGI_APPLICATION = 'django_template.wsgi.application'


DATABASES = {}

if config('DATABASE') == 'mysql':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('MYSQL_DATABASE_NAME'),
        'USER': config('MYSQL_USER'),
        'PASSWORD': config('MYSQL_PASSWORD')
    }
elif config('DATABASE') == 'postgresql':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRESQL_DATABASE_NAME'),
        'USER': config('POSTGRESQL_USER'),
        'PASSWORD': config('POSTGRESQL_PASSWORD')
    }
elif config('DATABASE') == 'sqlite':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'test': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'logs/test.log',
        }
    },
    'loggers': {
        'test': {
            'level': 'WARNING',
            'handlers': ['test'],
            'propagate': True
        }
    }
}

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


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = config('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Celery + Redis
REDIS_URL = config('REDIS_URL')
REDIS_PORT = '6379'

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_BROKER_URL = config('REDIS_URL')
CELERY_BACKEND_URL = config('REDIS_URL')
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = config('TIME_ZONE')
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = config('REDIS_URL') + '/0'
CELERY_RESULT_EXPIRES = 60

BROKER_URL = config('REDIS_URL')
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}

CELERYBEAT_SCHEDULE = {
}
