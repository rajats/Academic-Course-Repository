from django.conf.urls import patterns, include, url
from django.conf import settings 

urlpatterns = patterns('student.views',
	url(r'^courses/$','show_courses', name="show_courses"), 
    url(r'^enroll/(?P<id>.*)','enroll', name="enroll"),
    #url(r'^delete/(?P<id>.*)','delete_from_cart', name="delete_from_cart"),
)
