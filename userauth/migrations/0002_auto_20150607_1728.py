# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regprofessor',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='regstudent',
            name='branch',
        ),
        migrations.AddField(
            model_name='regprofessor',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='regstudent',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='regstudent',
            name='semester',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='regstudent',
            name='programme',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
