# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-07 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]
