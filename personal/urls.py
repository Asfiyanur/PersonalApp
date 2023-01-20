from django.urls import path
from .views import DepartmentView,PersonalListCreateView

urlpatterns = [
    path('department/',DepartmentView.as_view()),
    path('personal/',PersonalListCreateView.as_view()),
]

