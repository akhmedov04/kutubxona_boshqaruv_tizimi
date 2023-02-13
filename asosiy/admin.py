from django.contrib import admin
from .models import *

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "kurs", "kitoblar_soni", "bitiruvchi")
    list_display_links = ("id", "ism")
    list_editable = ("kurs", "kitoblar_soni", "bitiruvchi")
    list_filter = ("bitiruvchi", "kurs")
    list_per_page = 8
    search_fields = ("id", "ism")
    search_help_text = "Id va ism bo'yicha qidiradi"

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "yosh", "tirik", "kitob_soni", "jinsi", "tugulgan_sana")
    list_display_links = ("id", "ism")
    list_editable = ("kitob_soni", "tirik")
    list_filter = ("tirik",)
    search_fields = ("id", "ism", "tugulgan_sana")
    search_help_text = "Id, ism va tugulgan_sana bo'yicha qidirish"

# @admin.register(Kitob)
# class KitobAdmin(admin.ModelAdmin):



# admin.site.register(Muallif)
admin.site.register(Admin)
admin.site.register(Kitob)
admin.site.register(Record)
admin.site.register(Nashriyot)
admin.site.register(Kitobs)
admin.site.register(Sotuvchi)
admin.site.register(Sotuv)