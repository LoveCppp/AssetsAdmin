# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20170601_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iplist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('service', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('createtime', models.DateTimeField()),
            ],
            options={
                'db_table': 'iplist',
            },
        ),
    ]