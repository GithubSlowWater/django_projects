# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='访问路径'),
        ),
    ]
