import os.path
from pathlib import Path

from taskmaster_django_crm_project.postgress_pass import get_my_postgres_passwd, get_my_postgres_user, \
    get_my_postgres_hostname, get_my_postgres_port, get_my_secret_key
from django.template.context_processors import media
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
POSTGRES_USER = get_my_postgres_user()
POSTGRES_PASSWD = get_my_postgres_passwd()
POSTGRES_HOST = get_my_postgres_hostname()
POSTGRES_PORT = get_my_postgres_port()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_my_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # False

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    # django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # my apps:
    'taskmaster_django_crm_project.web_auth',
    'taskmaster_django_crm_project.taskmaster',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # my middlewares:
    'taskmaster_django_crm_project.web_auth.middleware.LoginRequiredMiddleware'
]

ROOT_URLCONF = 'taskmaster_django_crm_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
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

WSGI_APPLICATION = 'taskmaster_django_crm_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# # test sqlite3 database configuration:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# production postgresql database configuration:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "taskmaster",
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'taskmaster_django_crm_project/static_files',
    BASE_DIR / 'taskmaster_django_crm_project/static_files/css',
    BASE_DIR / 'taskmaster_django_crm_project/static_files/js',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'web_auth.AppUser'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'taskmaster_django_crm_project/media')

LOGIN_REDIRECT_URL = reverse_lazy('index')

LOGOUT_REDIRECT_URL = reverse_lazy('index')
