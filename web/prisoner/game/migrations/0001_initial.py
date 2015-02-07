# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prisoner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text="This is the prisoner's name. Enter your name :)", max_length=40)),
                ('strategy', models.CharField(help_text="This is the prisoner's strategy. Write it in Python.", max_length=1500)),
                ('years', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
