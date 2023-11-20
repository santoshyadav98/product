from django.contrib import admin
from smart.models import product
# Register your models here.

class smartadmin(admin.ModelAdmin):
    list_display=['pid','pname','pcost','pmfdt','pexpdt']

admin.site.register(product,smartadmin)