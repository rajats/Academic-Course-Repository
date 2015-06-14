# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_auto_20150614_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=1000, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(to='course.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
