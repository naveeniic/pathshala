from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    subjects = models.ForeignKey('Subjects', models.CASCADE)
    # fee = models.ForeignKey('fee', on_delete=models.CASCADE)


class ClassInfo(models.Model):
    section = models.CharField(max_length=2)
    room_id = models.CharField(max_length=10)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_teacher = models.ForeignKey('staff.Staff', on_delete=models.CASCADE)


class Subjects(models.Model):
    name = models.CharField(max_length=30)
    Description = models.TextField()
    reference = models.CharField(max_length=100)
    text_book = models.CharField(max_length=100)