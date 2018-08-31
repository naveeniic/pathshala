from rest_framework import serializers
from .models import Staff, Qualification, Experience


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'


class QualificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qualification
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = '__all__'


