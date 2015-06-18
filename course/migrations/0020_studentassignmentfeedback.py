# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_auto_20150619_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAssignmentFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_feedback', models.FileField(null=True, upload_to=b'studentassignmentsfeedbacks/files/', blank=True)),
                ('text_feedback', models.TextField(max_length=1000, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('student_assignment', models.ForeignKey(to='course.StudentAssignment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
