# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20180717_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='item',
            new_name='product',
        ),
    ]
