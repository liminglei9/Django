from django.contrib import admin
from .models import *
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','age']
    search_fields = ['name']
    list_filter = ['birthday']
admin.site.register(Person,PersonAdmin)
admin.site.register(Book)
admin.site.register(Publish)
# Register your models here.
