from django.shortcuts import render


from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Course, Lesson
# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_course = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_num")[:3]

        # 排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_course = all_course.order_by("-stdents")
            elif sort == "hot":
                all_course = all_course.order_by("-click_num")

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_course, 6, request=request)
        courses = p.page(page)

        return render(request, "course-list.html", {
            'all_course': courses,
            'sort': sort,
            'hot_courses': hot_courses
        })


class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 增加课程点击数
        course.click_num += 1
        course.save()

        # 相关课程推荐
        tag = course.tag
        if tag:
            relate_course = Course.objects.filter(tag=tag)[:1]
        else:
            relate_course = []
        return render(request, "course-detail.html", {
            'course': course,
            'relate_course': relate_course
        })