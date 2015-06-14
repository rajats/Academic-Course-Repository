# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20150613_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursenotice',
            name='title',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursenotice',
            name='content',
            field=models.TextField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
