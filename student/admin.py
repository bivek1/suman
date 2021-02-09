from django.contrib import admin
from .models import Principal, Staff, Student, CustomUser, attendance
# Register your models here.
admin.site.register(Principal)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(CustomUser)
admin.site.register(attendance)