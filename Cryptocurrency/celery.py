import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cryptocurrency.settings')

app = Celery('Cryptocurrency', broker_url='redis://localhost:6379')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print("))))))))))))))))))))))))))")
    print(f'Request: {self.request!r}')


# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'btc_realtime_price_tasks',
#         'schedule':crontab(),
#         'args': (16, 16)
#     },
# }

# app.conf.beat_schedule = {
#     #Scheduler Name
#     'btc_realtime_price_tasks': {
#         # Task Name (Name Specified in Decorator)
#         'task': 'btc_realtime_price_tasks',
#         # Schedule
#         'schedule': 2.0,
#         # Function Arguments
#     },
# }
