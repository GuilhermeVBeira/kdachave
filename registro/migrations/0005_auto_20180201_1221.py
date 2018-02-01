# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-01 14:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20180201_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
