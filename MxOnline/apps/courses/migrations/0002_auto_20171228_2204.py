# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coures',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='学习时长'),
        ),
    ]
