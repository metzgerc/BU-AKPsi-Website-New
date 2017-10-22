# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brothers', '0002_eboardmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='eboardmember',
            options={'verbose_name': 'Executive Board Member', 'verbose_name_plural': 'Executive Board Members'},
        ),
    ]