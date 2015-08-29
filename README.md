# Academic-Course-Repository
Visit the application live at: https://academicrepo.herokuapp.com

Academic Course Repository is a system where students of a college( IIITM ) can enroll in a course and access all course related materials all at one place.
This project is developed as part of my summer internship at ABV-IIITM Gwalior under the guidance of Dr. Rajendra Sahu.It is developed using django 1.7.4 and postgresql as database.

The aim of this project is to erase classroom boundries and to make everything related to a course available
online for students. It has following features:

1) A new student or professor account that is registered is not activated until the admin activates it.

2) A active student can get the list of courses in which he/she can enroll.Only that courses will be shown in which a student is eligible to enroll.Eligibility is decided using semester, programme and course type.

3) For elective courses of type 1,2,3, a student is allowed to enroll in only one course of that type i.e a student can enroll in one elective 1 type course,a student can enroll in one elective 2 type course,a student can enroll in one elective 3 type course.A student is allowed to leave a course if he/she has accidently
enrolled in it, this is needed because a student can't change elective type course without leaving a same elective type course.

4) A active student enrolled in a course can submit assignment online any number of times, only the last submission will be shown to the course instructor.If the deadline for an assignment has passed then the students will be disabled from submitting that assignment.

5) A professor who is instructor of the course(instructor of a course is assigned by admin) is allowed to add course notice, syllabus, lecture notes, assignment.A professor can view the submissions from each student who submitted the assignment.The instructor of the course can give feedback to each student individually
in form of file or comment.

6) A active student enrolled in a course can view the assignment feedback from the instructor and can also discuss the feedback with the instructor in form of comments.

*A add-on notification app will be added to notify students about new course material and to notify course instructor about submission.* 

*Although this system is designed for a particular college it can easily be used for any educational institution.* 