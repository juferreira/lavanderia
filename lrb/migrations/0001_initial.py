# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-03 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('unidade', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lrb.Apartamento')),
            ],
            options={
                'verbose_name_plural': 'Moradores',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('data_uso_maquina', models.DateTimeField(blank=True, primary_key=True, serialize=False)),
                ('data_criacao_reserva', models.DateTimeField(default=django.utils.timezone.now)),
                ('apartamento_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lrb.Apartamento')),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lrb.Maquina')),
            ],
        ),
    ]