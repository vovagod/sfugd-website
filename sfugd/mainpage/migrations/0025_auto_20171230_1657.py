# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-30 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0024_auto_20171230_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content_1',
            name='author',
        ),
        migrations.DeleteModel(
            name='Idea_en',
        ),
        migrations.DeleteModel(
            name='Info_en',
        ),
        migrations.DeleteModel(
            name='Content_1',
        ),
    ]
