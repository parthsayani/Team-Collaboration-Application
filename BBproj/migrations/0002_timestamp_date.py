# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-31 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBproj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timestamp',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]
