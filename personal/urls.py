from django.urls import path
from .views import DepartmentView,PersonalListCreateView,PersonalGetUpdateDelete

urlpatterns = [
    path('department/',DepartmentView.as_view()),
    path('personal/',PersonalListCreateView.as_view()),
    path('personal/<int:pk>/',PersonalGetUpdateDelete.as_view()),
]

