# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 10:05
from __future__ import unicode_literals

from django.db import migrations
import enumchoicefield.fields
import talent.models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='category',
            field=enumchoicefield.fields.EnumChoiceField(default=talent.models.TalentCategoryEnum(1), enum_class=talent.models.TalentCategoryEnum, max_length=50),
        ),
    ]
