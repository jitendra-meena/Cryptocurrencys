from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
from celery.utils.log import get_task_logger
from core.utils import get_btc_realtime_price, send_alert_email
from .models import BTCAlert
logger = get_task_logger(__name__)


@shared_task(name="btc_realtime_price_tasks")
def btc_realtime_price_tasks():
    print("_______________+______________________")
    logger.info("Let start----------")
    data = get_btc_realtime_price()
    price = data['current_price']
    btc = BTCAlert.objects.filter(price=price, price_status='created')
    if btc.exists():
        user = [alert.user.email for alert in btc]
        alert = [alert.id for alert in btc]
        if user:
            send_alert_email(user, price)
            for id in alert:
                BTCAlert.objects.filter(id=id).update(status='triggered')
            print("______triggered____")
    else:
        return "No Alert Found"
    return 'Success'


# @shared_task(name = "send_alert")
# def send_alert_to_user(user,price):
#     sent=send_alert_email(user,price)
#     return sent
