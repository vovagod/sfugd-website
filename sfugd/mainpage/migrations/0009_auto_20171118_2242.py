# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_auto_20171118_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_one',
            name='fafa_one',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='menu_one',
            name='item_one',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
