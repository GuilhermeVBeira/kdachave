# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-10 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_auto_20180110_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='bairro',
            field=models.CharField(default=123, max_length=30, verbose_name='Bairro'),
            preserve_default=False,
        ),
    ]
