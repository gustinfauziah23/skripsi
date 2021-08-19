from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(Ruangan)
admin.site.register(Petugas)
# admin.site.register(CekBarang)
admin.site.register(PindahBarang)
# admin.site.register(Pimpinan)


# Register your models here.

@admin.register(Barang)
class BarangAdmin(ImportExportModelAdmin):
    list_display = ("kode_barang", "nama_barang", "kondisi_barang", "lokasi", "jenis_barang",  "kategori_barang", "tanggal", "tgl_update", "status", "keterangan")
    pass 