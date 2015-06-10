# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_regprofessor_is_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regprofessor',
            name='is_professor',
        ),
    ]
