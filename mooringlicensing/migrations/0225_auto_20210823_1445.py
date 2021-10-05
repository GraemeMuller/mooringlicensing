# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-23 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0224_auto_20210823_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oraclecodeapplication',
            options={'verbose_name': 'Oracle Codes'},
        ),
        migrations.RemoveField(
            model_name='applicationtype',
            name='oracle_code',
        ),
        migrations.AlterField(
            model_name='oraclecodeitem',
            name='oracle_code_application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oracle_code_items', to='mooringlicensing.OracleCodeApplication'),
        ),
    ]
