# -*- coding: utf-8 -*-
__author__ = 'JK'
__date__ = '2019/1/17 23:51'

from django.conf.urls import url, include


from .views import CourseListView, CourseDetailView, CourseInfoView, CourseCommentView, AddComentsView

urlpatterns = [
    #课程机构首页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    # 课程章节详情
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CourseCommentView.as_view(), name="course_comment"),

    # 添加课程评论
    url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),
]