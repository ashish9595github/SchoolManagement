# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-18 11:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
