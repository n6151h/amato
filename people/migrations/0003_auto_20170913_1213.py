# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20170913_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='contact_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.ContactData'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='contact_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.ContactData'),
        ),
    ]
