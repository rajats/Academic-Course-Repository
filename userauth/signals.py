from django.dispatch import Signal

new_student = Signal(providing_args=['branch','programme','enroll_no'])
new_professor = Signal(providing_args=['branch',])