# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_content_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_one',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_one', models.CharField(max_length=20)),
            ],
        ),
    ]
