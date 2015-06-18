# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_auto_20150619_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassignment',
            name='student',
            field=models.ForeignKey(blank=True, to='userauth.RegStudent', null=True),
            preserve_default=True,
        ),
    ]
