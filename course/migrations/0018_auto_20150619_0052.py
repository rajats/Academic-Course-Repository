# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_studentassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignment',
            name='course_assignment',
            field=models.ForeignKey(blank=True, to='course.CourseAssignment', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentassignment',
            name='student',
            field=models.ForeignKey(to='userauth.RegStudent'),
            preserve_default=True,
        ),
    ]
