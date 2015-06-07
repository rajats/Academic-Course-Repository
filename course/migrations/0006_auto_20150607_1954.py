# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20150607_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='programme',
            field=multiselectfield.db.fields.MultiSelectField(max_length=50, choices=[(1, b'IPG( B.Tech + M.Tech in IT )'), (2, b'IPG(B.Tech (IT) + MBA)'), (3, b'M. Tech in Computer Science and Engineering (Digital Communication)'), (4, b'M. Tech in Computer Science and Engineering (Advanced Network)'), (5, b'M. Tech in Computer Science and Engineering (VLSI \xe2\x80\x93 Very Large Scale Integration)'), (6, b'M. Tech in Computer Science and Engineering (Information Security)'), (7, b'General MBA with specialization in Human Resources, Marketing and Finance'), (8, b'MBA in ITES'), (9, b'MBA in Public Service Management and e-Governance')]),
            preserve_default=True,
        ),
    ]
