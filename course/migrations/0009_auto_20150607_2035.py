# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20150607_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=multiselectfield.db.fields.MultiSelectField(max_length=20, choices=[(1, b'compulsary'), (2, b'elective')]),
            preserve_default=True,
        ),
    ]
