# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estufa', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Config_Padrao',
        ),
        migrations.RemoveField(
            model_name='log_irrigacao',
            name='slot',
        ),
        migrations.RemoveField(
            model_name='log_luminosidade',
            name='slot',
        ),
        migrations.RemoveField(
            model_name='log_temperatura',
            name='estufa',
        ),
        migrations.DeleteModel(
            name='Log_Irrigacao',
        ),
        migrations.DeleteModel(
            name='Log_Luminosidade',
        ),
        migrations.DeleteModel(
            name='Log_Temperatura',
        ),
    ]
