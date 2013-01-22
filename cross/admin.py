from django.contrib import admin
from models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'datetime', 'location','location_map_url']

class MailingListAdmin(admin.ModelAdmin):
    list_display = ['email_address']


admin.site.register(Event, EventAdmin)
admin.site.register(MailingList, MailingListAdmin)