# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20180717_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='updated',
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='update',
            field=models.BooleanField(default=False, verbose_name='修改数量'),
        ),
    ]
