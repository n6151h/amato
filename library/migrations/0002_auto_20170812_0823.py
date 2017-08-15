# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='type',
            field=models.IntegerField(choices=[(1, 'speaking'), (2, 'non-speakng'), (3, 'singing'), (0, 'unspecified')], default=0, verbose_name='Type'),
        ),
    ]