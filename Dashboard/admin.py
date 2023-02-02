from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis, Member

class kolomBarang(admin.ModelAdmin):
    list_display= ['kodebrg','nama','stok','harga','link_gbr','jenis_id']
    search_fields= ['kodebrg','nama']
    list_filter= ('jenis_id',)
    list_per_page= 3

admin.site.register(Barang,kolomBarang)
admin.site.register(Jenis)

class kolomMember(admin.ModelAdmin):
    list_display= ['nama','no_hp','provinsi','kota','kode_pos']
    search_fields= ['nama','provinsi']
    list_filter= ('nama',)
    list_per_page= 3

admin.site.register(Member,kolomMember)

