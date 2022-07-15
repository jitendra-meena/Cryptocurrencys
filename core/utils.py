from Cryptocurrency.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import json
import requests
from .models import BTCAlert


def send_alert_email(user,price):
    try:
        breakpoint()
        subject=f"Bitcoin Price Reached..."
        message = f""" BitCoin Price is reached {price}"""
        send_mail(subject,message,EMAIL_HOST_USER,[user],
        fail_silently= False)
        return True
    except:
        return False

def get_btc_realtime_price():
   
    response = requests.get(url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false?')
    json_response=response.json()
    data = json_response[0]
    return data