import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
# secret key : ...

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
    # local
    'home.apps.HomeConfig',
    'post.apps.PostConfig',
    'account.apps.AccountConfig',
    # third-party :
    'django_cleanup.apps.CleanupConfig',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'storages',
    'boto3',

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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'post.appcontext_processor.categories',

            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
    
# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
# STATIC_ROOT = '../../'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_URL = '/login/'
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Advanced',
    }
}


# storage :
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = '9d0d0a56-c95c-4391-a85c-4286a25df38e'
AWS_SECRET_ACCESS_KEY ='c87a1273a69f510ea72d747a661b6f8736f2255b4fccebd1a26c0a6040d8dcbe'
AWS_S3_ENDPOINT_URL = 'https://s3.ir-thr-at1.arvanstorage.com'
AWS_STORAGE_BUCKET_NAME = 'technerd'
AWS_SERVICE_NAME = 's3' #optional
AWS_S3_FILE_OVERWRITE = False #don't over write files wiht same name
