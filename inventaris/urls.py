from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter

#API
from django.urls import path, include

from rest_framework.routers import DefaultRouter
# from .views import *
from django.conf.urls import url

from .views import BarangViewSet, LoginViewSet, PindahViewSet, RegisterViewSet, RoomViewSet
from. views import InvViewSet




# router.register(r'cekbarang', CekViewSet, basename='cekbarang')
#

router = DefaultRouter()
# router.register('login', LoginViewSet, basename='login')
# router.register('register', RegisterViewSet, basename='register')

router.register(r'pindahbarang', PindahViewSet, basename='pindahbarang')
router.register(r'product', BarangViewSet, basename='product')
router.register(r'inventaris', InvViewSet, basename='inventaris')
router.register(r'room', RoomViewSet, basename='room')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewSet, basename='register')


urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('databarang/', views.databarang, name='databarang'),
    path('input-barang/', views.inputbarang, name='inputbarang'),
    path('update-barang/<str:pk>', views.updatebarang, name='updatebarang'),

    # Ruangan
    path('data-ruangan/', views.dataruangan, name='dataruangan'),
    path('input-ruangan/', views.inputruangan, name='inputruangan'),
    path('update-ruangan/<str:pk>', views.updateruangan, name='updateruangan'),

    path('perpindahan/', views.perpindahan, name='perpindahan'),
    path('pengecekan/', views.pengecekan, name='pengecekan'),
    path('peminjaman/', views.peminjaman, name='peminjaman'),
    path('pengembalian/', views.pengembalian, name='pengembalian'),

    # Fitur-fitur
    path('export-excel/', views.export, name='export'),
    path('upload-excel/', views.upload, name='upload'),
    path('tampil-qrcode/<str:pk>', views.tampil_qrcode, name='tampil_qrcode'),
    path('renderpdf-pengecekan/', views.render_pdf_pengecekan, name='renderpdf_pengecekan'),
    path('renderpdf-peminjaman/', views.render_pdf_peminjaman, name='renderpdf_peminjaman'),
    path('renderpdf-pengembalian/', views.render_pdf_pengembalian, name='renderpdf_pengembalian'),
    path('renderpdf-qrcode/<str:pk>', views.render_pdf_qrcode, name='renderpdf_qrcode'),
    path('laporan-perbulan/', views.laporan_bulan, name='laporan'),

    # Petugas
    path('profil/', views.profil, name='profil'),
    path('tambah-pengguna/', views.tambah_petugas, name='formpetugas'),
    path('form-pengguna/', views.datapengguna, name='datapengguna'),
    # Pimpinan
    path('pimpinan/', views.pimpinan, name='pimpinan'),
    path('profil-pimpinan/', views.profil_pimpinan, name='profil_pimpinan'),
    path('tambah-pimpinan/', views.tambah_pimpinan, name='formpimpinan'),
    path('data-inventaris/', views.data_inventaris, name='datainventaris'),
    path('dataruangan-pimpinan/', views.ruangan, name='ruangan'),
    path('halaman-qrcode/<str:pk>', views.qrcode, name='qr_code'),
    path('data-cek/', views.dtpengecekan, name='datapengecekan'),
    path('data-pindah/', views.dtperpindahan, name='dataperpindahan'),
    path('data-pinjam/', views.dtpeminjaman, name='datapeminjaman'),
    path('data-pengembalian/', views.dtpengembalian, name='datapengembalian'),
    path('data-petugas/', views.dtpetugas, name='data_petugas'),

    # LOGIN
    path('login-page/', views.loginPage, name='login'),
    path('logout-page/', views.logoutPage, name='logout'),

    path('', include(router.urls)),
    url(r'^upload/$', BarangViewSet, name='file-upload')


]
