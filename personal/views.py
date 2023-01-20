from django.shortcuts import render
from .serializers import DepartmentSerializers
from rest_framework import generics
from .models import Department,Personal
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStafforReadOnly

# Create your views here.


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializers
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated,IsStafforReadOnly]