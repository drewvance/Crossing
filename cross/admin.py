from django.contrib import admin
from models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'datetime', 'location','location_map_url']


admin.site.register(Event, EventAdmin)