# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0018_idea_sec'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea_sec',
            name='linkname_part',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
