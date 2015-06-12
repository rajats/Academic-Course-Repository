from django.conf.urls import patterns, include, url
from django.conf import settings 

urlpatterns = patterns('course.views',
	url(r'^view-course/(?P<id>.*)','view_course', name="view_course"), 
	url(r'^add-assignment/(?P<id>.*)','add_assignment', name="add_assignment"), 
	url(r'^add-syllabus/(?P<id>.*)','add_syllabus', name="add_syllabus"), 
	url(r'^add-lecture-notes/(?P<id>.*)','add_lecture_notes', name="add_lecture_notes"), 
	url(r'^add-notice/(?P<id>.*)','add_notice', name="add_notice"), 
)
