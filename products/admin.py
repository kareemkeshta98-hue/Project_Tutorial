from django.contrib import admin
from.models import product,Test

# Register your models here.
class productadmin (admin.ModelAdmin):
    # للظهور جنب اسم المنتج:
    list_display = ['name','price','active','Category']
    # لتحويل هذة الفئات للينك بمجرد الضغط:
    list_display_link = ['name','price']
    # لاتاحه التعديل من الخارج : 
    list_editable = ['Category','active']
    #  لاضافة سيرش :
    search_fields=['name','price']
    # لاضافة فلتر بحث :
    list_filter=['Category']



admin.site.register(product,productadmin)
admin.site.register(Test)

#  تعديل الاسم في الادمن بانل
admin.site.site_header = "Tutorial"
admin.site.site_title = "Tutorial"
