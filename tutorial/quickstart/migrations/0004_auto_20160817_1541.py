# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-17 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20160817_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='age',
            field=models.IntegerField(),
        ),
    ]
