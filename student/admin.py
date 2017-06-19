from django.contrib import admin
from .models import Classroom, Duty, Student


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_editable = ('description',)
    list_filter = ('name', )


class DutyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_editable = ('description',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'name', 'phone', 'email', 'classroom', 'status', 'duty')
    list_editable = ('status',)
    empty_value_display = '学生'


admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Student, StudentAdmin)
