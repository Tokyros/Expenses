# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager', '0004_auto_20160903_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='started_working',
            field=models.DateField(null=True, verbose_name='Date of Hire'),
        ),
    ]
