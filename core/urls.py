from django.urls import path
from .views import *
urlpatterns = [
    path('api/alert/get/',AlertList.as_view(),name='alert-get'),
    path('api/alert/create/',CreateAlert.as_view(),name='alert-create'),
    path('api/alert/delete/<int:id>/',AlertDelete.as_view(),name='alert-mutation'),
]
