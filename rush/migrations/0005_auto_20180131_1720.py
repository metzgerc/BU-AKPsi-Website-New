# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 17:20
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0004_auto_20180118_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rushprofile',
            name='major_schools',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=6), size=None),
        ),
    ]