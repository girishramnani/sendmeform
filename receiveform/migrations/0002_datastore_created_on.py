# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-24 09:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('receiveform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datastore',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 24, 9, 43, 28, 127404, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
