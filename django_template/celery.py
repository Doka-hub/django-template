from celery import Celery

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_template.settings')


app = Celery('django_template')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
