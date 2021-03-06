# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 12:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0004_auto_20170908_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBackOthers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreign_mood', models.CharField(max_length=250)),
                ('foreign_reason', models.CharField(max_length=500)),
                ('date_feedback', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date_feedback',
            field=models.CharField(max_length=500),
        ),
    ]
