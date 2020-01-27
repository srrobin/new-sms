from rest_framework import serializers

from teacher.models import TeacherInfo
from teacher.models import Designation


from student.models import StudentClassInfo
from student.models import StudentShiftInfo
from student.models import Gender
from student.models import Section
from student.models import Session
from student.models import StudentInfo
from student.models import StudentDetailsInfo



class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClassInfo
        fields = '__all__'

class StudentShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentShiftInfo
        fields = '__all__'

class StudentGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class StudentSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class StudentSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'

class StudentDetailsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailsInfo
        fields = '__all__'



#teacher  Serializer

class TeacherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherInfo
        fields = '__all__'


class TeacherDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

