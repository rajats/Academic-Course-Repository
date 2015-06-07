# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20150607_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(default=b'compulsary', max_length=20, choices=[(1, b'compulsary'), (2, b'elective')]),
            preserve_default=True,
        ),
    ]
