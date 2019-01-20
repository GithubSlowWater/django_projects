# -*- coding: utf-8 -*-
__author__ = 'JK'
__date__ = '2019/1/17 23:51'

from django.conf.urls import url, include


from .views import CourseListView, CourseDetailView

urlpatterns = [
    #课程机构首页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

]