# # from django.contrib.auth.models import
# import django_filters
# from django_filters import DateFilter
# from .models import *

# class BarangFilter(django_filters.FilterSet):
#     tglmulai = DateFilter(field_name="tanggal", lookup_expr='gte')
#     tglakhir = DateFilter(field_name="tanggal", lookup_expr='lte')

#     class Meta :
#         model = Barang
#         fields = ['jenis_barang', 'kategori_barang']