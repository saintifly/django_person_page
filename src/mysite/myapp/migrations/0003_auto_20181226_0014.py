# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-25 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20181221_2200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '\u5546\u54c1', 'verbose_name_plural': '\u6211\u7684\u5546\u54c1'},
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(blank=True, default='normal.png', null=True, upload_to='images', verbose_name='\u5546\u54c1\u56fe\u7247'),
        ),
    ]
