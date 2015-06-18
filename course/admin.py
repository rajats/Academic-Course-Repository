from django.contrib import admin
from .models import Course, CourseAssignment, CourseSyllabus, CourseLectureNotes, CourseNotice, CourseFeedback, StudentAssignment

admin.site.register(Course)
admin.site.register(CourseAssignment)
admin.site.register(CourseSyllabus)
admin.site.register(CourseLectureNotes)
admin.site.register(CourseNotice)
admin.site.register(CourseFeedback)
admin.site.register(StudentAssignment)
