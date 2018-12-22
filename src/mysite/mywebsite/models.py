# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mywebsite(models.Model):
    sitename = models.CharField('sitename',max_length=30,blank=True,null=True)
    desc = models.URLField('desc', max_length=200,blank=True,null=True)
    class Meta:
        verbose_name = "网站"
        verbose_name_plural = "我的网站"
        app_label = 'mywebsite'
    def __unicode__(self):
        return self.sitename
		
def __str__(self):
    return self.name