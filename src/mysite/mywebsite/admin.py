# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from mywebsite.models import Mywebsite
from django.utils.safestring import mark_safe 

class AuthorAdmin(admin.ModelAdmin):
    def Desc(self,obj):
        a = '<a href="%s" >%s</a>'%(obj.desc,obj.desc)
        return mark_safe(a)

    list_display = ('sitename', 'Desc', 'Getto')
    search_fields = ('sitename', 'desc')
   # list_editable=('sitename',)
    
    list_filter = ('sitename',)
    #fields = ('sitename', 'desc')
    fieldsets = [
        (None,               {'fields': ['sitename']}),
        (None,               {'fields': ['desc']}),
    ]
    def Getto(self,obj):
        a = '<a href="%s" target="_blank">点击跳转</a>'%obj.desc
        return mark_safe(a)
admin.site.register(Mywebsite,AuthorAdmin)
