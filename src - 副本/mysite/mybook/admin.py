# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from mybook.models import Books

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('bookname', 'bookstarttime',\
                    'bookinfo', 'booktype','bookendtime','bookremark')
    search_fields = ('bookname', 'bookinfo')
    list_filter = ('bookname',)
    fields = ('bookname', 'booktype', 'bookstarttime', 'bookendtime',\
              'bookinfo', 'bookremark')
admin.site.register(Books,AuthorAdmin)

