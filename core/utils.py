from Cryptocurrency.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import json
import requests
from .models import BTCAlert

def get_realtime_price():
    """
    get_realtime_price: used for getting realtime price of BTC from coingecko API
    """
    breakpoint()
    response = requests.get(url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false?')
    json_response=response.json()
    data = json_response[0]
    return data


def send_alert_email(receivers,price):
    try:
        subject=f"Alert !! Bitcoin Price Reached..."
        message = f""" 
        Hello User
        BitCoin Price is reached to {price}
        """
        send_mail(subject,message,EMAIL_HOST_USER,[receivers],
        fail_silently= False)
        return True
    except:
        return False

def trigger(alerts):
    try:
        for alert in alerts:
            BTCAlert.objects.filter(id=alert).update(status='triggered')
            return True
    except:
        return False

def get_alert(price):
    alerts=BTCAlert.objects.filter(price=price,status='created')
    return alerts