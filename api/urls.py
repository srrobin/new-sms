from django.urls import path

from .views import TeacherApiView
from .views import TeacherDesignationApiView
from .views import TeacherApiDetailView
from .views import TeacherNewApiView

from .views import StudentApiView
from .views import StudentClassApiView
from .views import StudentApiDetailView
from .views import StudentNewApiView





urlpatterns = [
    path('teacher/designation/', TeacherDesignationApiView.as_view()),
    path('teacher/detail', TeacherApiView.as_view()),
    path('teacher/<int:pk>/', TeacherApiDetailView.as_view()),
    path('teacher/new/', TeacherNewApiView.as_view()),

    path('student/class/', StudentClassApiView.as_view()),
    path('student/detail', StudentApiView.as_view()),
    path('student/<int:pk>/', StudentApiDetailView.as_view()),
    path('student/new/', StudentNewApiView.as_view()),
]