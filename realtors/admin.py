from django.contrib import admin
from realtors.models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','hire_date','email')
    list_display_links = (4, 'name')
    search_fields = ('name')
    list_per_page = 20
admin.site.register(Realtor)