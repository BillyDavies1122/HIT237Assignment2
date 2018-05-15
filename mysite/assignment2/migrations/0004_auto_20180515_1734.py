# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-15 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2', '0003_auto_20180515_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='assignment2.publisher'),
        ),
        migrations.AlterField(
            model_name='game',
            name='systemRequirements',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='assignment2.systemRequirements'),
        ),
    ]