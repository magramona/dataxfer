# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oh_data_source', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='openhumansmember',
            name='last_xfer_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='openhumansmember',
            name='last_xfer_status',
            field=models.TextField(blank=True),
        ),
    ]
