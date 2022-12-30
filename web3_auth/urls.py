# -*- coding:utf-8 -*-
"""
Created on 2022/12/30 20:53
@File: urls.py
---------
@summary:
---------
@Author: clark
@Email: clark1203@foxmail.com
"""
from django.urls import path

from . import views

urlpatterns = [
    path('moralis_auth', views.moralis_auth, name='moralis_auth'),
    path('request_message', views.request_message, name='request_message'),
    path('my_profile', views.my_profile, name='my_profile'),
    path('verify_message', views.verify_message, name='verify_message')
]