# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20150608_0004'),
        ('userauth', '0002_auto_20150607_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courses', models.ManyToManyField(to='course.Course')),
                ('name', models.ForeignKey(to='userauth.RegStudent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
