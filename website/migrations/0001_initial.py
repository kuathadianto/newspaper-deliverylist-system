# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('datei', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Strasse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strassenname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zusatzinformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beschreibung', models.CharField(max_length=500)),
                ('bild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Bild')),
            ],
        ),
        migrations.CreateModel(
            name='Zusatztext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Zustellung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hausnummer', models.IntegerField()),
                ('summe_zeitungen', models.IntegerField()),
                ('strasse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Strasse')),
            ],
        ),
        migrations.AddField(
            model_name='zusatzinformation',
            name='information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Zusatztext'),
        ),
        migrations.AddField(
            model_name='zusatzinformation',
            name='zustellung',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Zustellung'),
        ),
    ]