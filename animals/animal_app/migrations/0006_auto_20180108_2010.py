# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-09 01:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal_app', '0005_auto_20180108_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={},
        ),
        migrations.AlterModelOptions(
            name='part',
            options={'ordering': ['pk']},
        ),
    ]