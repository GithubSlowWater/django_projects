# -*- coding: utf-8 -*-
__author__ = 'JK'
__date__ = '2019/1/16 21:27'

from django import forms
from  operation.models import UserAsk


class UserAskForm(forms.ModelForm):
     class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
