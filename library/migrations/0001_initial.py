# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 02:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enumchoicefield.fields
import library.models
import people.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('published', models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(1300)])),
                ('synopsis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('role_type', enumchoicefield.fields.EnumChoiceField(default=library.models.RoleTypeEnum(4), enum_class=library.models.RoleTypeEnum, max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Musical',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.Book')),
                ('composer', models.CharField(max_length=100)),
                ('lyricist', models.CharField(max_length=100)),
            ],
            bases=('library.book',),
        ),
        migrations.CreateModel(
            name='Opera',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.Book')),
                ('composer', models.CharField(max_length=100)),
                ('librettist', models.CharField(max_length=100)),
            ],
            bases=('library.book',),
        ),
        migrations.CreateModel(
            name='OperaticRole',
            fields=[
                ('role_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.Role')),
                ('voice', enumchoicefield.fields.EnumChoiceField(default=people.models.VoiceTypeEnum(1), enum_class=people.models.VoiceTypeEnum, max_length=12)),
                ('fach', enumchoicefield.fields.EnumChoiceField(default=people.models.FachEnum(1), enum_class=people.models.FachEnum, max_length=11)),
            ],
            bases=('library.role',),
        ),
        migrations.CreateModel(
            name='Oratorio',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.Book')),
                ('composer', models.CharField(max_length=100)),
            ],
            bases=('library.book',),
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.Book')),
                ('author', models.CharField(max_length=100)),
            ],
            bases=('library.book',),
        ),
        migrations.AddField(
            model_name='role',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='library.Book'),
        ),
    ]
