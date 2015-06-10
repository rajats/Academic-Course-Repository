# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_auto_20150609_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='regprofessor',
            name='is_professor',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
