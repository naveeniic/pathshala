# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Student, Address, ParentInfo
from .serializers import StudentSerializer, AddressSerializer, ParentInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentList(APIView):
    """
    List all student information, or create a new one
    """
    def get(self, request, format=None):
        student_data = Student.objects.all()
        serializer = StudentSerializer(student_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print request.META
        if self.request.META['CONTENT_TYPE'] == 'application/json':
            request_json = self.request.data
            if request_json:
                serializer = StudentSerializer(data=request_json)
                if serializer.is_valid():
                    serializer.save()
                    return Response(dict(result=True), status=status.HTTP_201_CREATED)
                return Response(dict(result=False))
            return Response(dict(result=False, detail="no data found in request"))
        if self.request.META['CONTENT_TYPE'] == 'application/x-www-form-urlencoded':
            request_form = self.request.POST.copy()
            if request_form:
                serializer = StudentSerializer(data=request_form)
                if serializer.is_valid():
                    serializer.save()
                    return Response(dict(result=True), status=status.HTTP_201_CREATED)
                return Response(dict(result=False))



