from django.shortcuts import render
from .serializers import DepartmentSerializers
from rest_framework import generics
from .models import Department,Personal

# Create your views here.


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializers
    queryset = Department.objects.all()