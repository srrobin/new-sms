from django.contrib import admin
from .models import TeacherInfo
from .models import Gender
from .models import Designation

admin.site.register(Gender)
admin.site.register(Designation)
admin.site.register(TeacherInfo)

