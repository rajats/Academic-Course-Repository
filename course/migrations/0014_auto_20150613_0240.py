# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_coursesyllabus_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseassignment',
            old_name='deccription',
            new_name='description',
        ),
    ]
