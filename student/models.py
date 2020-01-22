from django.db import models

class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=10)
    class_short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.class_name


class StudentShiftInfo(models.Model):
    shift_name= models.CharField(max_length=20)

    def __str__(self):
        return self.shift_name


class Gender(models.Model):
    gender_name= models.CharField(max_length=20)

    def __str__(self):
        return self.gender_name


class Section(models.Model):
    section_name= models.CharField(max_length=20)

    def __str__(self):
        return self.section_name


class Session(models.Model):
    session_name = models.CharField(max_length=4)

    def __str__(self):
        return self.session_name


class StudentInfo(models.Model):
    name= models.CharField(max_length=20)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return self.name


class StudentDetailsInfo(models.Model):
    roll_no = models.IntegerField()
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    std_class = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    std_shift = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    std_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    std_session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

