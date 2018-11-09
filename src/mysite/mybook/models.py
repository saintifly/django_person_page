# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Books(models.Model):
    bookname = models.CharField('bookname',max_length=200,null=False)
    bookstarttime = models.CharField('bookstarttime',max_length=30)
    bookinfo = models.CharField('bookinfo', max_length=200)
    booktype = models.CharField('booktype',max_length=30)
    bookendtime = models.CharField('bookendtime', max_length=30)
    bookremark = models.CharField('bookremark',max_length=1000)
    def __unicode__(self):
        return self.bookname

def __str__(self):
    return self.name