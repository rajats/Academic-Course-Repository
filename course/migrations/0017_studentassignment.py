# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_remove_regprofessor_is_professor'),
        ('course', '0016_coursefeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAssignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment', models.FileField(upload_to=b'studentassignments/files/')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(to='course.Course')),
                ('student', models.ForeignKey(blank=True, to='userauth.RegStudent', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
