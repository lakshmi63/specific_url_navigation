from django.urls import path
from app2.views import *
app_name='maa'

urlpatterns=[
    path('vara/',vara,name='vara'),
]