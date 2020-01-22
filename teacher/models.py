from django.db import models


class Gender(models.Model):
    title = models.CharField(max_length= 50)

    def __str__(self):
        return self.title


class Designation(models.Model):
    title = models.CharField(max_length= 50)

    def __str__(self):
        return self.title

class TeacherInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
