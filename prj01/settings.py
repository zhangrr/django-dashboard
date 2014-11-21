"""
Django settings for prj01 project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '839*7q5&d!xv3#3w3sh*31o1gl99@h-*yo0$1-ois5*_u3k!p8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_toolkit',
    'login',
    'dashboard',
    'my_tasks',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'prj01.urls'

WSGI_APPLICATION = 'prj01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'django',                       
        'USER': 'django',  
        'PASSWORD': 'djtest',  
        'HOST': 'localhost',                        
        'PORT': '3306',                        
    }  
}

BROKER_URL = "amqp://songxr:IloveU@localhost:5672/vhost"
CELERY_RESULT_BACKEND = "db+mysql://django:djtest@localhost/django"
#CELERY_RESULT_BACKEND = "amqp"
#CELERY_RESULT_BACKEND = "db+sqlite:///results.db"
#CELERY_RESULT_BACKEND = "db+mysql://scott:tiger@localhost/foo"
#CELERY_RESULT_BACKEND = "db+postgresql://scott:tiger@localhost/mydatabase"
#CELERY_RESULT_BACKEND = "db+oracle://scott:tiger@127.0.0.1:1521/sidname"
#CELERYD_CONCURRENCY = 1
#CELERYD_NODES="w1"
CELERY_IMPORTS = (
    'my_tasks.tasks',
    'dashboard.views',
)
#CELERY_TASK_RESULT_EXPIRES = 1200
#CELERYD_CONCURRENCY = 50
#CELERYD_PREFETCH_MULTIPLIER = 4 
#CELERYD_MAX_TASKS_PER_CHILD = 40 
#CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler' 

CELERY_QUEUES = {
    "default_songxr": { 
        "exchange": "default_songxr",
        "exchange_type": "direct",
        "routing_key": "default_songxr"
    },
    "topicqueue": { 
        "exchange": "topic_exchange",
        "exchange_type": "topic",
        "routing_key": "topictest.#",
    },
    "test1": { 
        "exchange": "broadcast_tasks",
        "exchange_type": "fanout",
        "binding_key": "broadcast_tasks1",
    },
    "test2": {
        "exchange": "broadcast_tasks",
        "exchange_type": "fanout",
        "binding_key": "broadcast_tasks2",
    },
}

class MyRouter(object):
    def route_for_task(self, task, args=None, kwargs=None):
        print("ROUTE FOR TASK: %r" % (task, ))
        if task.startswith('my_tasks'):
            return {
                "exchange": "default_songxr",
                "exchange_type": "direct",
                "routing_key": "default_songxr"
            }
        elif task.startswith('dashboard'):
            return {
                "exchange": "default_songxr",
                "exchange_type": "direct",
                "routing_key": "default_songxr"
            }
        elif task.startswith('topictest'):
            return {
                'queue': 'topicqueue',
            }
        elif task.startswith('dongwm.tasks.test'):
            return {
                "exchange": "broadcast_tasks",
            }
        else:
            return None
CELERY_ROUTES = (MyRouter(), )

import djcelery
djcelery.setup_loader()

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
BOOTSTRAP_BASE_URL = os.path.join(STATIC_URL, 'bootstrap/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

