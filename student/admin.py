from django.contrib import admin
from .models import StudentClassInfo,StudentShiftInfo,Gender,Section,StudentInfo,StudentDetailsInfo,Session


admin.site.register(StudentClassInfo)
admin.site.register(StudentShiftInfo)
admin.site.register(Gender)
admin.site.register(Section)
admin.site.register(Session)
admin.site.register(StudentInfo)
admin.site.register(StudentDetailsInfo)


