# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20170718_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zusatzinformation',
            name='bild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Bild'),
        ),
    ]