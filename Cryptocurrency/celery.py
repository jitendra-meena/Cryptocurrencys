import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cryptocurrency.settings')

app = Celery('Cryptocurrency',broker_url='redis://redis:6379')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')