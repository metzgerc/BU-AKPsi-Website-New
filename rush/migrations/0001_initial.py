# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RushEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('room_number', models.CharField(help_text='Ex. "Backcourt" for GSU Background or "209" for PHO 209', max_length=20, verbose_name='Room Number or Name')),
                ('room_long_name', models.CharField(help_text='Example: Photonics Center Auditorium (for PHO 206)', max_length=50, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('description', models.TextField(help_text='Use HTML tags to bold or italicize text.Note: Use the same description for both infosessions.')),
            ],
        ),
        migrations.CreateModel(
            name='RushEventLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=5)),
                ('lat', models.DecimalField(decimal_places=6, help_text='Put building name into https://www.latlong.net/ for lat/lng', max_digits=8, verbose_name='Latitude')),
                ('lng', models.DecimalField(decimal_places=6, help_text='See above', max_digits=8, verbose_name='Longitude')),
            ],
        ),
        migrations.AddField(
            model_name='rushevent',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rush.RushEventLocation'),
        ),
        migrations.CreateModel(
            name='Rush FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name': 'Rush FAQ',
                'verbose_name_plural': 'Rush FAQs',
            },
        ),
    ]
