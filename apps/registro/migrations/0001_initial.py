# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-22 00:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('propriedade', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoa', '0001_initial'),
        ('molho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEntrega', models.DateTimeField(verbose_name='Data Entrega')),
                ('dataPrevisaoRetorno', models.DateTimeField(verbose_name='Data de Previsão do Retorno')),
                ('dataRetorno', models.DateTimeField(blank=True, null=True, verbose_name='Data Retorno')),
                ('molhos', models.ManyToManyField(to='molho.Molho')),
                ('propriedade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propriedade.Propriedade')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsavel', to='pessoa.Pessoa')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]