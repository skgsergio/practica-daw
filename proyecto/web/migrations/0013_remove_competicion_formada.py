# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20150526_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competicion',
            name='formada',
        ),
    ]
