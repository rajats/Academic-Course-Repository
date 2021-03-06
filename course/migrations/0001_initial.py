# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20150607_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=50, choices=[(1, b'IPG( B.Tech + M.Tech in IT )'), (2, b'IPG(B.Tech (IT) + MBA)'), (3, b'M. Tech in Computer Science and Engineering (Digital Communication)'), (4, b'M. Tech in Computer Science and Engineering (Advanced Network)'), (5, b'M. Tech in Computer Science and Engineering (VLSI \xe2\x80\x93 Very Large Scale Integration)'), (6, b'M. Tech in Computer Science and Engineering (Information Security)'), (7, b'General MBA with specialization in Human Resources, Marketing and Finance'), (8, b'MBA in ITES'), (9, b'MBA in Public Service Management and e-Governance')])),
                ('instructor', models.ForeignKey(to='userauth.RegProfessor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
