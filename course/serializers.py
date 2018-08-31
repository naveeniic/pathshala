from rest_framework import serializers
from .models import Course, ClassInfo, Subjects


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class ClassInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassInfo
        fields = '__all__'


class SubjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = '__all__'

