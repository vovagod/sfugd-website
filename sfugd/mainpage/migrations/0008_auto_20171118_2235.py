# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_auto_20171118_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_one',
            name='html_one',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
