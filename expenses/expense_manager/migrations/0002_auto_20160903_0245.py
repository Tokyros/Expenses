# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 23:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='started_working',
            field=models.DateField(default=datetime.datetime(2016, 9, 2, 23, 45, 49, 788914, tzinfo=utc), verbose_name='Date of Hire'),
        ),
    ]