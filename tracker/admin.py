from django.contrib import admin
from .models import CategoryOption, Entry, VrajLocation

# Register your earlier models
admin.site.register(CategoryOption)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('some_text', 'category', 'time_start', 'time_stop')
    list_filter = ('category', 'time_start')
    search_fields = ('some_text', 'comments')

# Register your new model
@admin.register(VrajLocation)
class VrajLocationAdmin(admin.ModelAdmin):
    list_display = ('kha_paya_gya_tha', 'kis_jagah', 'time_kya_tha')