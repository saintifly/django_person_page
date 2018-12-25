# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from myapp.models import Goods

from django.utils.safestring import mark_safe 



class AuthorAdmin(admin.ModelAdmin):
    def Picture(self,obj):
		try:
			img = mark_safe('<img src="%s" width="50px" />' % (obj.picture,))
		except Exception as e:
			img = ''
		return img
    Picture.short_description = 'Thumb'
    Picture.allow_tags = True
	
    list_display = ('title', 'price', 'desc','unit','Picture','detail',)
    search_fields = ('title', 'desc')
    readonly_fields = ('Picture',)
   # list_editable=('sitename',)
    
    list_filter = ('title',)
    #fields = ('sitename', 'desc')

admin.site.register(Goods,AuthorAdmin)



# admin.site.site_url = 'www.baidu.com'

# Register your models here.
# from blog.models import Blog
  
#Blog模型的管理器
# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ('id', 'caption', 'author', 'publish_time')
#     
#     #list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 50
#     
#     #ordering设置默认排序字段，负号表示降序排序
#     ordering = ('-publish_time',)
#   
#     #list_editable 设置默认可编辑字段
#     list_editable = ['machine_room_id', 'temperature']
#   
#     #fk_fields 设置显示外键字段
#     fk_fields = ('machine_room_id',)
#     
#     list_filter =('trouble', 'go_time', 'act_man__user_name', 'machine_room_id__machine_room_name') #过滤器
#     search_fields =('server', 'net', 'mark') #搜索字段
#     date_hierarchy = 'go_time'    # 详细时间分层筛选　
    
#class MyAdminSite(admin.AdminSite):
#    site_header = '个人网站管理系统'  # 此处设置页面显示标题
#    site_title = '个人网站'  # 此处设置页面头部标题
  
#admin_site = MyAdminSite(name='management')
admin.site.site_header = '个人网站管理系统'
admin.site.site_title = '个人网站'