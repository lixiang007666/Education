# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-06 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20180102_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='coures',
            name='is_tg',
            field=models.BooleanField(default=False, verbose_name='课程首页推广'),
        ),
    ]
