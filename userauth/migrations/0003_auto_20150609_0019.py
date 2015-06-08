# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20150607_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regstudent',
            name='enroll_no',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
