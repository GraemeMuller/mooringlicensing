# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-26 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0037_merge_20210326_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vesselownership',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=5),
        ),
    ]
