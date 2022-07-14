from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .utils import get_realtime_price


class AlertList(APIView):
    permission_classes = [AllowAny]
    serializer_class = AlertListSerializer
    def get(self, request, format=None):
        get_realtime_price()
        alert = BTCAlert.objects.all()
        serializer = AlertListSerializer(alert,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        




class CreateAlert(APIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = AlertListSerializer
    def post(self, request, format=None):
        try:
            serializer = AlertListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class AlertDelete(APIView):
    def delete(self, request, id):
        alert = BTCAlert.objects.get(id = id)
        data = {'status':'deleted'}
        serializer = DeleteAlertSerializer(alert,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

