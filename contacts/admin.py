from django.contrib import admin

from django.apps import apps

# Register your models here.
from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','listings')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listings',)
    list_per_page = 25


 # for model in models:
 #     try:
 #         admin.site.register(model)
 #     except admin.sites.AlreadyRegistered:
 #
 #        pass

