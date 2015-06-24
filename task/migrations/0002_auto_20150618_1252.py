# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='added',
            field=models.DateTimeField(default=datetime.date(2015, 6, 18), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.date(2015, 6, 18), verbose_name=b'Due date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(default=datetime.date(2015, 6, 18), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
