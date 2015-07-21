# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150706_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='key_expires',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
