# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20180717_1415'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='CartModel',
        ),
    ]