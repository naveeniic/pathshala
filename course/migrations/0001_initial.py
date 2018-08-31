# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-11 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=2)),
                ('room_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Description', models.TextField()),
                ('reference', models.CharField(max_length=100)),
                ('text_book', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subjects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Subjects'),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
    ]
