from django.conf.urls import patterns, include, url
from django.conf import settings 

urlpatterns = patterns('userauth.views',
    #url(r'^login/','signin', name="login"),
    url(r'^login/', 'signin', name="login"),
    url(r'^logout/','signout', name="logout"),
    url(r'^register-student/','register_student', name="register_student"),
    url(r'^register-professor/','register_professor', name="register_professor"),
)
