# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20150611_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesyllabus',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
