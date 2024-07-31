import os
from celery import Celery


"""
Initializing Celery
Celery-Django configuration is in settings.py
"""


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')

app = Celery('assignment')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Loading task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')