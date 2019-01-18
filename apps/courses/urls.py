# -*- coding: utf-8 -*-
__author__ = 'JK'
__date__ = '2019/1/17 23:51'

from django.conf.urls import url, include


from .views import CourseListView

urlpatterns = [
    #课程机构首页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

]