# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prisoner',
            name='years',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
