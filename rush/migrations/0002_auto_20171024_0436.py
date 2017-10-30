# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rushevent',
            options={'ordering': ['start_time'], 'verbose_name': 'Event'},
        ),
        migrations.AlterModelOptions(
            name='rusheventlocation',
            options={'verbose_name': 'Event Location'},
        ),
        migrations.AlterField(
            model_name='rushevent',
            name='room_number',
            field=models.CharField(help_text='Ex. "Backcourt" for GSU Backcourt or "209" for PHO 209', max_length=20, null=True, verbose_name='Room Number or Name'),
        ),
        migrations.AlterField(
            model_name='rusheventlocation',
            name='abbreviation',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
