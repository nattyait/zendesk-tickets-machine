# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assignee_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='requester_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
