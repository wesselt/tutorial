# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0010_remove_feedback_date_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date_first',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
