from datetime import datetime

from django.db import models
from organization.models import CourseOrg, Teacher
# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name="课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    teacher = models.ForeignKey(Teacher, verbose_name="讲师", default="", null=True, blank=True)
    degree = models.CharField(choices=(("cj","初级"),("zj", "中级"), ("gj","高级")),max_length=10,verbose_name="课程难度")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(单位分钟)")
    stdents = models.IntegerField(default=0, verbose_name="学习人数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)
    click_num = models.IntegerField(default=0, verbose_name="课程点击数")
    category = models.CharField(default="后端开发",max_length=30, verbose_name="课程类别")
    tag = models.CharField(default=" ",max_length=30, verbose_name="课程标签-")
    youneed_know = models.CharField(max_length=300, default="", verbose_name="课程须知")
    teacher_tell = models.CharField(max_length=300, default="", verbose_name="老师告诉你能学到什么")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        return self.lesson_set.all().count()

    def get_learn_user(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=50, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_course_video(self):
        # 获取章节视频
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(max_length=50, verbose_name="视频名")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(单位分钟)")
    url =  models.CharField(max_length=200, default="", verbose_name="访问路径")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=50, verbose_name="视频名")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name