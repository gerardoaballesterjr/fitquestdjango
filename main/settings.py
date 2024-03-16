from pathlib import Path
from datetime import timedelta
from dotenv import dotenv_values

env = dotenv_values('.env')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(env['SECRET_KEY'])

DEBUG = eval(env['DEBUG'])

ALLOWED_HOSTS = str(env['ALLOWED_HOSTS']).split(';')

INSTALLED_APPS = [
    'core',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'drf_spectacular',
    'cloudinary',
    'django_cleanup',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "TOKEN_OBTAIN_SERIALIZER": "core.api.auth.views.LoginView",
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Fit Quest API Documentation',
    'DESCRIPTION': 'Lorem ipsum...',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': str(env['DB_ENGINE']),
        'NAME': str(env['DB_NAME']),
        'USER': str(env['DB_USER']),
        'PASSWORD': str(env['DB_PASSWORD']),
        'HOST': str(env['DB_HOST']),
        'PORT': int(env['DB_PORT']),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = False

STATIC_URL = 'staticfiles/'

STATICFILES_DIRS = [BASE_DIR / 'staticfiles']

MEDIA_URL = 'mediafiles/'

MEDIA_ROOT = BASE_DIR / 'mediafiles'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': str(env['CLOUDINARY_STORAGE_CLOUD_NAME']),
    'API_KEY': str(env['CLOUDINARY_STORAGE_API_KEY']),
    'API_SECRET': str(env['CLOUDINARY_STORAGE_API_SECRET']),
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.User'