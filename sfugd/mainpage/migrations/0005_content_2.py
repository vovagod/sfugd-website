# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20171022_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_2', models.TextField()),
            ],
        ),
    ]