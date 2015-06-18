# encoding=utf8
import os

from django.db import models

from multiselectfield import MultiSelectField

from userauth.models import RegProfessor, RegStudent

class Course(models.Model):
	name = models.CharField(max_length=100)
	PROGRAMME_CHOICES = [(1,'IPG( B.Tech + M.Tech in IT )'),(2,'IPG(B.Tech (IT) + MBA)'),\
		(3,'M. Tech in Computer Science and Engineering (Digital Communication)'),\
		(4,'M. Tech in Computer Science and Engineering (Advanced Network)'),\
		(5,'M. Tech in Computer Science and Engineering (VLSI – Very Large Scale Integration)'),\
		(6,'M. Tech in Computer Science and Engineering (Information Security)'),\
		(7,'General MBA with specialization in Human Resources, Marketing and Finance'),\
		(8,'MBA in ITES'),(9,'MBA in Public Service Management and e-Governance')]
	programme = MultiSelectField(choices=PROGRAMME_CHOICES, max_choices=2, max_length=50)
	instructor = models.ForeignKey(RegProfessor, null=True, blank=True)
	semester = models.IntegerField(default=1)
	COURSE_TYPE_CHOICES = [(1,'compulsary'),(2,'elective 1'),(3,'elective 2'), (4,'elective 3')]
	course_type = MultiSelectField(choices=COURSE_TYPE_CHOICES, max_choices=1, max_length=20)

	def __unicode__(self):
		return '%s of semester %s and programme %s' % (self.name,self.semester,self.get_programme_display())

	def show_name_type(self):
		return '%s (type %s)' % (self.name,self.get_course_type_display())

	def show_course_type(self):
		return '%s' %(self.get_course_type_display())

class CourseAssignment(models.Model):
	course = models.ForeignKey(Course)
	description = models.CharField(max_length=100, null=True, blank=True)
	assignment = models.FileField(upload_to="assignments/files/")
	deadline = models.DateTimeField('deadline', null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)

	def file_link(self):
		if self.assignment:
			return self.assignment.url
		else:
			return "No attachment"

class CourseSyllabus(models.Model):
	course = models.ForeignKey(Course)
	syllabus = models.FileField(upload_to="syllabus/files/")
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)

	def file_link(self):
		if self.syllabus:
			return self.syllabus.url
		else:
			return "No attachment"

class CourseLectureNotes(models.Model):
	course = models.ForeignKey(Course)
	lecture_notes = models.FileField(upload_to="lecturenotes/files/")
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)

	def file_link(self):
		if self.lecture_notes:
			return self.lecture_notes.url
		else:
			return "No attachment"

class CourseNotice(models.Model):
	course = models.ForeignKey(Course)
	title = models.CharField(max_length=20, null=True, blank=True)
	content = models.TextField(max_length=1000, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)

class CourseFeedback(models.Model):
	course = models.ForeignKey(Course)
	content = models.TextField(max_length=1000, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)

class StudentAssignment(models.Model):
	course = models.ForeignKey(Course)
	student = models.ForeignKey(RegStudent, null=True, blank=True)
	course_assignment = models.ForeignKey(CourseAssignment,null=True, blank=True)
	assignment = models.FileField(upload_to="studentassignments/files/")
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)

	def file_link(self):
		if self.assignment:
			return self.assignment.url
		else:
			return "No attachment"

class StudentAssignmentFeedback(models.Model):
	student_assignment = models.ForeignKey(StudentAssignment)
	file_feedback =  models.FileField(upload_to="studentassignmentsfeedbacks/files/", null=True, blank=True)
	text_feedback = models.TextField(max_length=1000, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)

	def file_link(self):
		if self.file_feedback:
			return self.file_feedback.url
		else:
			return "No attachment"

