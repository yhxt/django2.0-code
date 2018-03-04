from django.contrib import admin
from .models import ReadNum


class ReadNumAdmin(admin.ModelAdmin):
    list_display=('id','read_num','content_object')

admin.site.register(ReadNum,ReadNumAdmin)
