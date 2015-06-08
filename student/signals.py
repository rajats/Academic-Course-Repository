from django.dispatch import Signal

new_student_course = Signal(providing_args=['student'])