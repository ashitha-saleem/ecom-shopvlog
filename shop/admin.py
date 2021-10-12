from django.contrib import admin
from . models import categ,products

# Register your models here.
class categadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,categadmin)

class prodadmin(admin.ModelAdmin):
    list_display=['name','slug','img','stock','price','desc']
    list_editable=['img','stock','price','desc']
    prepopulated_fields={'slug':('name',)}
admin.site.register(products,prodadmin)