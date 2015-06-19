# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0020_studentassignmentfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAssignmentFeedbackComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=1000, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('commenter', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('student_assignment', models.ForeignKey(to='course.StudentAssignment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
