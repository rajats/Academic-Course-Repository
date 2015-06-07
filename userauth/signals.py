from django.dispatch import Signal

new_student = Signal(providing_args=['programme','enroll_no','semester'])
new_professor = Signal(providing_args=[])