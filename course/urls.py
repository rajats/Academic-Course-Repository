from django.conf.urls import patterns, include, url
from django.conf import settings 

urlpatterns = patterns('course.views',
	url(r'^view-course/(?P<id>.*)','view_course', name="view_course"), 
	url(r'^view-assignment/(?P<id>.*)','view_assignment', name="view_assignment"), 
	url(r'^add-assignment/(?P<id>.*)','add_assignment', name="add_assignment"), 
	url(r'^view-syllabus/(?P<id>.*)','view_syllabus', name="view_syllabus"), 
	url(r'^add-syllabus/(?P<id>.*)','add_syllabus', name="add_syllabus"), 
	url(r'^view-lecture-notes/(?P<id>.*)','view_lecture_notes', name="view_lecture_notes"), 
	url(r'^add-lecture-notes/(?P<id>.*)','add_lecture_notes', name="add_lecture_notes"), 
	url(r'^add-notice/(?P<id>.*)','add_notice', name="add_notice"), 
	url(r'^view-feedback/(?P<id>.*)','view_feedback', name="view_feedback"), 
	url(r'^add-feedback/(?P<id>.*)','add_feedback', name="add_feedback"), 
	url(r'^submit-assignment/(?P<c_id>[-\w]+)/(?P<a_id>[-\w\ ]+)/$','submit_assignment', name="submit_assignment"), 
	url(r'^view-submitted-assignments/(?P<c_id>[-\w]+)/(?P<a_id>[-\w\ ]+)/$','view_submitted_assignment', name="view_submitted_assignment"), 
	url(r'^add-assignment-feedback/(?P<c_id>[-\w]+)/(?P<sa_id>[-\w]+)/(?P<form_type>[-\w\ ]+)/$','add_assignment_feedback', name="add_assignment_feedback"), 	
)
