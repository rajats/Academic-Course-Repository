from django.conf.urls import patterns, include, url
from django.conf import settings 

urlpatterns = patterns('professor.views',
	url(r'^courses/$','my_teaching_courses', name="my_teaching_courses"), 
)
