# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager', '0003_auto_20160903_0246'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='portfolio',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
