from import_export import resources
from .models import Barang 

class BarangResource(resources.ModelResource):
    class Meta:
        model = Barang
        # fields= '__all__'
        # exclude = ['nama_user', 'gambar', 'qrcode']S