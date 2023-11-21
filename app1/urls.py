from django.urls import path

from app1.views import *
app_name='varamma'
urlpatterns=[
    path('maa/',maa,name='maa'),
]