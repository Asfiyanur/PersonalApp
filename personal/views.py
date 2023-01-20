from django.shortcuts import render
from .serializers import DepartmentSerializers,PersonalSerializer,DepartmentPersonalSerializer
from rest_framework import generics,status
from .models import Department,Personal
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsStafforReadOnly,IsOwnerAndStaffOrReadOnly

# Create your views here.


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializers
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated,IsStafforReadOnly]
    
class PersonalListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()
    permission_classes = [IsAuthenticated,IsStafforReadOnly]
    
    #? buradaki create ve perform_createler ListCreateApiView in func larından alındı
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.request.user.is_staff:
            personnel = self.perform_create(serializer)
            data = {
                "message": f"Personal {personnel.first_name} saved successfully",
                "personnel" : serializer.data
            }
        else:
            data = {
                "message": "Yetkiniz yoktur.."
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        person = serializer.save()
        # !burada yapılan create  serializerdaki 28.satırdaki create işleminin aynısını yerine getiricek
        person.create_user = self.request.user
        person.save()
        return person
    
class PersonalGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class=PersonalSerializer
    # permission_classes = [IsAuthenticated,IsOwnerAndStaffOrReadOnly]
    permission_classes = [IsAuthenticated]

# ! IsOwner permssion ı kapatsak bile put u override ederek aynı contional i elde ebiliriz / delete de sadce superuser a verebililriz bu şekilde

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_staff and (instance.create_user == self.request.user):
            return self.update(request, *args, **kwargs)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        
        
    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        
        
class DepartmentPersonalView(generics.ListAPIView):
    serializer_class = DepartmentPersonalSerializer
    queryset = Department.objects.all()
    
    def get_queryset(self):
        name = self.kwargs["department"]
        return Department.objects.filter(name__iexact=name)
    
    
class Custom(generics.RetrieveAPIView):
    serializer_class = DepartmentPersonalSerializer
    queryset = Department.objects.all()
    lookup_field= "name"