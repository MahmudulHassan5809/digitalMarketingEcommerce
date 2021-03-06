import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l7l6)zj8t#&yh1m_e4r613i+r)vxz*_z2=l+u(o4t^k3wy%j&$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'taggit',
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',


    'authentication',
    'store',
    'cart',

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

ROOT_URLCONF = 'myproject.urls'

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
                'store.context_processor.categories',
                'store.context_processor.all_tag',
                'store.context_processor.wishlist_length',
                'cart.context_processor.cart_total_amount'
            ],

        },

    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

CART_PRODUCT_MODEL = 'store.models.Product'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
FORCE_STATIC_FILE_SERVING = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myproject/static')
]


# Media settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


JQUERY_URL = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'


CKEDITOR_UPLOAD_PATH = "ck_editor/"
CKEDITOR_RESTRICT_BY_USER = True


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': '100%'
    }
}


CART_SESSION_ID = 'cart'

BATON = {
    'SITE_HEADER': 'DigitalService Admin',
    'SITE_TITLE': 'DigitalService Admin Admin Portal',
    'INDEX_TITLE': 'Welcome to DigitalService Admin Researcher Portal',
    'SUPPORT_HREF': 'https://github.com/MahmudulHassan5809',
    'COPYRIGHT': 'copyright © 2019 <a href="https://github.com/MahmudulHassan5809">Mahmudul Hassan</a>',  # noqa
    'POWERED_BY': '<a href="https://github.com/MahmudulHassan5809">Mahmudul Hassan</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'MENU': (
        {'type': 'title', 'label': 'main', 'apps': ('auth', )},
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        {
            'type': 'app',
            'name': 'authentications',
            'label': 'Accounts',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'profile',
                    'label': 'Profiles'
                },
            )
        },
        {
            'type': 'app',
            'name': 'store',
            'label': 'Store',
            'icon': 'fa fa-store',
            'models': (
                {
                    'name': 'category',
                    'label': 'Categories'
                },
                {
                    'name': 'product',
                    'label': 'Products'
                },
                {
                    'name': 'store',
                    'label': 'Stores'
                },
            )
        },
        # {
        #     'type': 'app',
        #     'name': 'taggit',
        #     'label': 'Taggit',
        #     'icon': 'fa fa-tag',
        #     'models': (
        #         {
        #             'name': 'tags',
        #             'label': 'Tags'
        #         },
        #     )
        # },
        {
            'type': 'app',
            'name': 'cart',
            'label': 'Cart',
            'icon': 'fa fa-shopping-cart',
            'models': (
                {
                    'name': 'order',
                    'label': 'Orders'
                },
                {
                    'name': 'transactionmethod',
                    'label': 'Transaction Methods'
                },

            )
        },

    ),
}
