# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0010_cont_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='Start_sec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_sec_one', models.CharField(max_length=100, null=True)),
                ('start_text_one', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cont_start',
        ),
    ]
