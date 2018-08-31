# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=2)
    dob = models.DateField()
    photo = models.ImageField(upload_to='')
    parent_info = models.ForeignKey('ParentInfo', on_delete=models.CASCADE)
    p_address = models.ForeignKey('Address', related_name='permanent_address', on_delete=models.CASCADE)
    t_address = models.ForeignKey('Address', related_name='temporary_address', on_delete=models.CASCADE)
    class_id = models.ForeignKey('course.ClassInfo', on_delete=models.CASCADE)


class ParentInfo(models.Model):
    p_type = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    occupation = models.CharField(max_length=30)
    qualificaton = models.CharField(max_length=100)
    email = models.EmailField()
    office = models.CharField(max_length=100)


class Address(models.Model):
    Add_type = models.CharField(max_length=2)
    House_No = models.CharField(max_length=10)
    street = models.CharField(max_length=10)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
