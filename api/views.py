from rest_framework import generics,permissions

from teacher.models import TeacherInfo
from teacher.models import Designation

from .serializers import TeacherInfoSerializer
from .serializers import TeacherDesignationSerializer


from student.models import StudentClassInfo
from student.models import StudentShiftInfo
from student.models import Gender
from student.models import Section
from student.models import Session
from student.models import StudentInfo
from student.models import StudentDetailsInfo

from .serializers import StudentInfoSerializer
from .serializers import StudentClassSerializer


#student view
class StudentApiView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = StudentDetailsInfo.objects.all()
    serializer_class = StudentInfoSerializer

class StudentClassApiView(generics.ListAPIView):
    queryset = StudentClassInfo.objects.all()
    serializer_class = StudentClassSerializer

class StudentApiDetailView(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = (permissions.IsAuthenticated,)
     queryset = StudentInfo.objects.all()
     serializer_class = StudentInfoSerializer

class StudentNewApiView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = StudentInfo.objects.all().order_by('-id')[:1]
    serializer_class = StudentInfoSerializer





#teacher view
class TeacherApiView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TeacherInfo.objects.all()
    serializer_class = TeacherInfoSerializer

class TeacherDesignationApiView(generics.ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = TeacherDesignationSerializer

class TeacherApiDetailView(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = (permissions.IsAuthenticated,)
     queryset = TeacherInfo.objects.all()
     serializer_class = TeacherInfoSerializer

class TeacherNewApiView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TeacherInfo.objects.all().order_by('-id')[:1]
    serializer_class = TeacherInfoSerializer
