# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-20 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default=' ', max_length=30, verbose_name='课程标签-'),
        ),
    ]
