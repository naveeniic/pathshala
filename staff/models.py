from __future__ import unicode_literals

from django.db import models


class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=2)
    dob = models.DateField()
    grade = models.CharField(max_length=20)
    date_of_join = models.DateField()
    role = models.CharField(max_length=30)
    subjects = models.ForeignKey('course.Subjects', on_delete=models.CASCADE)
    Address = models.ForeignKey('student.Address', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='')


class Qualification(models.Model):
    qualificaton = models.CharField(max_length=20)
    board = models.CharField(max_length=80)
    percentage = models.IntegerField()
    year_of_passing = models.DateField()
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)


class Experience(models.Model):
    tenure = models.IntegerField()
    designation = models.CharField(max_length=50)
    organisation = models.CharField(max_length=100)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
