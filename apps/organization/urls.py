# -*- coding: utf-8 -*-
__author__ = 'JK'
__date__ = '2019/1/16 21:34'

from django.conf.urls import url, include
from .views import OrglistView, AddUserAskView

urlpatterns = [
    #课程机构首页
    url(r'^list/$', OrglistView.as_view(), name="org_list"),
    url(r'^add_ask', AddUserAskView.as_view(), name="add_ask")
]