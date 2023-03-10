from django.urls import path
from .views import DepartmentView,PersonalListCreateView,PersonalGetUpdateDelete,DepartmentPersonalView,Custom

urlpatterns = [
    path('department/',DepartmentView.as_view()),
    path('personal/',PersonalListCreateView.as_view()),
    path('personal/<int:pk>/',PersonalGetUpdateDelete.as_view()),
    # path('department/<str:department>/',DepartmentPersonalView.as_view()),
    path('department/<str:name>/',Custom.as_view()),
]

