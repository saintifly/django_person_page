# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-21 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='desc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detail',
            field=models.CharField(blank=True, default='\u5546\u54c1\u8be6\u60c5', max_length=1000, null=True, verbose_name='\u5546\u54c1\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(blank=True, default='normal.png', null=True, upload_to='static/images/goods', verbose_name='\u5546\u54c1\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='\u5546\u54c1\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='unit',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u5355\u4f4d'),
        ),
    ]