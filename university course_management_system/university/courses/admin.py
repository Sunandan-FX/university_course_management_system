from django.contrib import admin
from .models import Student, Instructor, Course, Enrollment



class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'enrollment_date')
    search_fields = ('name',)
    list_filter = ('department',)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'hire_date', 'courses_count')

    def courses_count(self, obj):
        return obj.courses.count()
    courses_count.short_description = "Courses Taught"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'title', 'credits', 'instructor', 'enrolled_students_count')
    inlines = [EnrollmentInline]

    def enrolled_students_count(self, obj):
        return obj.enrollments.count()
    enrolled_students_count.short_description = "Enrolled Students"


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'grade')
    list_filter = ('course', 'enrollment_date')
    search_fields = ('student__name', 'course__title')
