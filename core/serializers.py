from dataclasses import field, fields
from rest_framework import serializers
from .models import BTCAlert


class AlertListSerializer(serializers.ModelSerializer):

    class Meta:
        model =BTCAlert
        fields = ['user','price','price_status']


class DeleteAlertSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BTCAlert
        fields = ['price_status']