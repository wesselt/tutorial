# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 14:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_moods'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Moods',
        ),
    ]
