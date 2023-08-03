from django.urls import path,include
from .views import StudentList,StudentDetail


urlpatterns = [
    path('students/', StudentList.as_view(), name='list_students'),
    path('students/<int:pk>', StudentDetail.as_view(), name='students_Detail'),

]