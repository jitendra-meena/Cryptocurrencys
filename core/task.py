from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
from celery.utils.log import get_task_logger
from core.utils import get_realtime_price,send_alert_email,trigger,get_alert

logger = get_task_logger(__name__)


@shared_task(name = "get_realtime_price_tasks")
def get_realtime_price_tasks():
   
    data=get_realtime_price()
    price=data['current_price']
    name=data['name']

    logger.info(f"fetched Price of Bitcoin!! is {price}")
    # alerts=Alert.objects.filter(price=price,status='created')
    alerts=get_alert(price)
    if alerts.exists():
        receivers=[alert.user.email for alert in alerts]
        alert=[alert.id for alert in alerts]

        if len(receivers)>0:
            send_alert_to_user.delay(receivers,price)
            is_triggered=trigger(alert)
            print(is_triggered)

    else:
        print(f"No Alert Match...!")

    return 'Success'

    


@shared_task(name = "send_alert")
def send_alert_to_user(receivers,price):
    """
    
    send_alert_to_user: Sending Alert Using Email
    """
    is_sent=send_alert_email(receivers,price)
    return is_sent
