from django.contrib import admin
from django.utils.html import format_html
from .models import Service
from django.contrib.auth.models import Group
# Register your models here.
admin.site.site_header = "Mr Cool Admin"
admin.site.site_title = "Mr Cool Dashboard"
admin.site.index_title = "Welcome to Mr Cool Admin Panel"
admin.site.unregister(Group)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    def service_img(self , obj):
        return format_html('<img src="{}" width="100" height="100">'.format(obj.image.url))
    list_display = ('name', 'service_img')

    
