from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from .models import *
from .forms import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator
# from .filters import BarangFilter
from inventaris.resources import BarangResource
from tablib import Dataset
from xhtml2pdf import pisa
from django.template.loader import get_template

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
#api
from .serializers import BarangDescriptiveSerializer, BarangSerializer, InvSerializer, PindahSerializer, RoomDescriptiveSerializer, RoomSerializer, UserAccountSerializer
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.authtoken.models import Token
from rest_framework import viewsets



from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login

# Create your views here.
@login_required(login_url='login')
@pilihan_login
def beranda(request):
    # dt_petugas = Petugas.objects.all()
    databarang = Barang.objects.all()
    total_barang = Barang.objects.count()
    total_barangmasuk = databarang.filter(jenis_barang = 'Barang Masuk').count()
    total_barangkeluar = databarang.filter(jenis_barang = 'Barang Keluar').count()
    total_barangrusak = databarang.filter(jenis_barang = 'Barang Rusak').count()
    barang_habispakai = databarang.filter(kategori_barang = 'Barang Habis Pakai').count()
    tidak_habispakai = databarang.filter(kategori_barang = 'Barang Tidak Habis Pakai').count()
    total_peminjaman = databarang.filter(status='Di Pinjam').count()
    total_pengembalian = databarang.filter(status='Di Kembalikan').count()
    context = {
        "menu" : 'Beranda',
        # "page" : 'Selamat Datang di Aplikasi Inventaris'
        'dt_barang' : databarang,
        'barang_inventaris' : total_barang,
        'barangmasuk' : total_barangmasuk,
        'barangkeluar' : total_barangkeluar,
        'barangrusak' : total_barangrusak,
        'habispakai' : barang_habispakai,
        'tidakhabispakai' : tidak_habispakai,
        'peminjaman' : total_peminjaman,
        'pengembalian' : total_pengembalian,
        # 'petugas' : dt_petugas


    }
    return render(request, 'inventaris/beranda.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def databarang(request):
    data = Barang.objects.order_by('-kode_barang')
    list_barang = Barang.objects.all() 
    halaman_tampil = Paginator(list_barang, 3)
    halaman_url = request.GET.get('halaman', 1)
    halaman_barang = halaman_tampil.get_page(halaman_url)
    
    if halaman_barang.has_previous():
        url_previous = f'?halaman={halaman_barang.previous_page_number()}'
    else:
        url_previous = ''
            
    if halaman_barang.has_next():
        url_next = f'?halaman={halaman_barang.next_page_number()}'
    else:
        url_next = ''
    context = {
        "menu" : 'Data Inventaris',
        "page" : 'Data Inventaris',
        'barang' : data,
        'halaman_list_barang' : halaman_barang,
        'previous' : url_previous,
        'next' : url_next,

    }
    return render(request, 'inventaris/databarang.html', context)

# Laporan Perbulan
def laporan_bulan(request):
    if 'tgl_update' in request.GET:
        chek = request.GET['tgl_update']
        tampil_data = Barang.objects.filter(tgl_update=chek)
    else:
        tampil_data = Barang.objects.filter(tgl_update=None)       

    context = {
        'tampil_data': tampil_data,
        }
    return render(request, 'inventaris/laporan_bulan.html',  context) 


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def inputbarang(request):
    if request.method == 'POST' :
        kode_barang = request.POST.get('kode_barang')

        if Barang.objects.filter(kode_barang = kode_barang).first():
            messages.success(request, 'Kode Barang Sudah Ada')
            return redirect('inputbarang')

        form = BarangForm(data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            obj=form.instance
            return redirect('databarang')
            return render(request, 'inventaris/inputbarang.html', {"obj":obj})

    else:
        form=BarangForm()
    foto = Barang.objects.all()

    return render(request, 'inventaris/inputbarang.html', {"foto":foto, "form":form})

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def updatebarang(request, pk):
    up_barang = Barang.objects.get(id=pk)
    form = BarangForm(instance = up_barang)
    if request.method == 'POST':
        form = BarangForm(request.POST, request.FILES, instance=up_barang)
        if form.is_valid:
            form.save()
            return redirect('databarang')

    context = {
        "menu" : 'Update Data Barang',
        "page" : 'Form Update Data Barang',
        'form': form 
    }
    return render(request, 'inventaris/updatebarang.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def dataruangan(request):
    dt_ruangan = Ruangan.objects.order_by('-kode_ruangan')
    context = {
        'menu' : 'Data Ruangan',
        'page' : 'Halaman Data Ruangan',
        'ruangan' : dt_ruangan
    }
    return render(request, 'inventaris/dataruangan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def inputruangan(request):
    inputruangan = RuanganForm()
    if request.method == 'POST' :
        kode_ruangan = request.POST.get('kode_ruangan')

        if Ruangan.objects.filter(kode_ruangan = kode_ruangan).first():
            messages.success(request, 'Kode Ruangan Sudah Ada')
            return redirect('inputruangan')

        form = RuanganForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dataruangan')

    context = {
        "menu" : 'Input Data Ruangan',
        "page" : 'Form Data Ruangan',
        'form' : inputruangan
    }
    return render(request, 'inventaris/inputruangan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def updateruangan(request, pk):
    up_ruangan = Ruangan.objects.get(id=pk)
    form = RuanganForm(instance = up_ruangan)
    if request.method == 'POST':
        form = RuanganForm(request.POST, request.FILES, instance=up_ruangan)
        if form.is_valid:
            form.save()
            return redirect('dataruangan')

    context = {
        "menu" : 'Update Data Ruangan',
        "page" : 'Form Update Data Ruangan',
        'form': form 
    }
    return render(request, 'inventaris/updateruangan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def perpindahan(request):

    dt_pindah = PindahBarang.objects.all()
    dt_lokasilama = Inventaris.objects.filter().order_by('-barang_id')

    context = {
    "menu" : 'Perpindahan Barang',
    "page" : 'Data Perpindahan Barang',
    'pindah' : dt_pindah
    
    }
    return render(request, 'inventaris/perpindahan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def pengecekan(request):
    context = {
    "menu" : 'Pengecekan Barang',
    "page" : 'Data Pengecekan Barang'  
    }
    return render(request, 'inventaris/pengecekan.html', context)


@login_required(login_url='login')
@pilihan_login
def peminjaman(request):
    dt_peminjaman = Inventaris.objects.filter(status = 'Di Pinjam')

    context = {
        'menu' : 'Data Peminjaman',
        'page' : 'Halaman Peminjaman',
        # 'filter_data_barang' : filter,
        'peminjaman' : dt_peminjaman
    }
    return render(request, 'inventaris/peminjaman.html', context)

@login_required(login_url='login')
@pilihan_login
def pengembalian(request):
    dt_pengembalian = Inventaris.objects.filter(status  = 'Di Kembalikan')
    context = {
        'menu' : 'Data Pengembalian',
        'page' : 'Halaman Pengembalian',
        'pengembalian' : dt_pengembalian
    }
    return render(request, 'inventaris/pengembalian.html', context)

@login_required(login_url='login')
@pilihan_login
def tampil_qrcode(request, pk):
    obj = Barang.objects.get(id=pk)
    kode_barang = "kode_barang"

    context = {
        "menu" : 'Cetak QR Code',
        "page" : 'Halaman Cetak QR Code',
        'obj' : obj,
        'kode_barang' : kode_barang,
    }
    return render(request, 'inventaris/tampilqrcode.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def export(request):
    barang_resource = BarangResource()  
    dataset = barang_resource.export()
    #response = HttpResponse(dataset.csv, content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="member.csv"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data Barang.xls"'

    return response

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def upload(request):
    if request.method == 'POST':
        barang_resource = BarangResource()
        dataset = Dataset()
        new_barang = request.FILES['myfile']

        if not new_barang.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_barang.read(),format='xls')
        for data in imported_data:
            value = Barang(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10]
                )
            value.save()
    return render(request, 'upload.html')

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def render_pdf_pengecekan(request):
    pengecekan = CekBarang.objects.all
    context = {
        'pengecekan': pengecekan,
        }
    return render(request, 'inventaris/pdf_pengecekan.html',  context) 

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def render_pdf_peminjaman(request):
    peminjaman = Inventaris.objects.filter(status  = 'Di Pinjam')
    context = {
        'peminjaman': peminjaman,
        }
    return render(request, 'inventaris/pdf_peminjaman.html',  context) 

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def render_pdf_pengembalian(request):
    pengembalian = Inventaris.objects.filter(status  = 'Di Kembalikan')
    context = {
        'pengembalian': pengembalian,
        }
    return render(request, 'inventaris/pdf_pengembalian.html',  context) 

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def render_pdf_qrcode(request, pk):
    obj = Barang.objects.get(id=pk)

    context = {'obj': obj}
    return render(request, 'inventaris/pdf_qrcode.html', context)

    # obj = Barang.objects.get(id=pk)
    # template_path = 'inventaris/pdf_qrcode.html'
    # context = {'obj' : obj}

    # # Untuk download PDF
    # response = HttpResponse(content_type='application/pdf')
    # # Untuk menampilkan 
    # response['Content-Disposition'] = 'filename = "QR Code.pdf"'

    # template = get_template(template_path)
    # html = template.render(context) 

    # # Buat PDF
    # pisa_status = pisa.CreatePDF(
    #     html, dest = response)
    # if pisa_status.err:
    #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def tambah_petugas(request):
    form = PetugasForm()
    formpetugas = PetugasForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username = username).first():
            messages.success(request, 'Nama pengguna sudah ada')
            return redirect('formpetugas')

        if password1 != password2:
            messages.success(request, 'Kata sandi tidak sama! silahkan coba kembali ')
            return redirect('formpetugas')

        # user
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.is_active = True
        user.save()
        # user
        # Group
        inventaris_petugas = Group.objects.get(name='petugas')
        user.groups.add(inventaris_petugas)
        # Group
        # inventaris_pimpinan = Group.objects.get(name='pimpinan')
        # user.groups.add(inventaris_pimpinan)
        # Petugas
        formsimpanpetugas = formpetugas.save()
        formsimpanpetugas.user = user
        formsimpanpetugas.save()  
    context = {
        'menu' : 'Form Pengguna',
        'page' : 'form pengguns',  
        'form' : form,      
    }
    return render(request, 'inventaris/tambah_petugas.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def profil(request):
    datapetugas = request.user.petugas
    form = PetugasForm(instance = datapetugas)
    if request.method == 'POST':
        form = PetugasForm(request.POST, request.FILES, instance=datapetugas)
        if form.is_valid:
            form.save() 
    context = {
        'menu': 'Profil',
        'page' : 'Halaman Profil',
        'formpetugas': form
    }
    return render(request, 'inventaris/profil.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def datapengguna(request):
    dt_pengguna = Petugas.objects.all()
    context = {
        'menu' : 'Data Pengguna',
        'page' : 'Halaman Data Pengguna',
        'petugas' : dt_pengguna
    }
    return render(request, 'inventaris/datapengguna.html', context)

@login_required(login_url='login')
def pimpinan(request):
    databarang = Barang.objects.all()
    total_barang = Barang.objects.count()
    total_barangmasuk = databarang.filter(jenis_barang = 'Barang Masuk').count()
    total_barangkeluar = databarang.filter(jenis_barang = 'Barang Keluar').count()
    total_barangrusak = databarang.filter(jenis_barang = 'Barang Rusak').count()
    barang_habispakai = databarang.filter(kategori_barang = 'Barang Habis Pakai').count()
    tidak_habispakai = databarang.filter(kategori_barang = 'Barang Tidak Habis Pakai').count()
    total_peminjaman = databarang.filter(status='Di Pinjam').count()
    total_pengembalian = databarang.filter(status='Di Kembalikan').count()
    context = {
        "menu" : 'Beranda',
        # "page" : 'Selamat Datang di Aplikasi Inventaris'
        'dt_barang' : databarang,
        'barang_inventaris' : total_barang,
        'barangmasuk' : total_barangmasuk,
        'barangkeluar' : total_barangkeluar,
        'barangrusak' : total_barangrusak,
        'habispakai' : barang_habispakai,
        'tidakhabispakai' : tidak_habispakai,
        'peminjaman' : total_peminjaman,
        'pengembalian' : total_pengembalian,

    }
    return render(request, 'inventaris/pimpinan/beranda_pimpinan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def tambah_pimpinan(request):
    form = PetugasForm()
    formpimpinan = PetugasForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username = username).first():
            messages.success(request, 'Username sudah ada')
            return redirect('formpimpinan')

        if password1 != password2:
            messages.success(request, 'Password Tidak sama')
            return redirect('formpimpinan')
        # user
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.is_active = True
        user.save()
        # user
        # Group
        inventaris_pimpinan = Group.objects.get(name='pimpinan')
        user.groups.add(inventaris_pimpinan)
        # Group

        # Petugas
        formsimpanpimpinan = formpimpinan.save()
        formsimpanpimpinan.user = user
        formsimpanpimpinan.save()  
    context = {
        'menu' : 'Form Pimpinan',
        'page' : 'form pimpinan',  
        'form' : form,      
    }
    return render(request, 'inventaris/pimpinan/tambah_pimpinan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def profil_pimpinan(request):
    datapimpinan = request.user.pimpinan
    form = PimpinanForm(instance = datapimpinan)
    if request.method == 'POST':
        form = PimpinanForm(request.POST, request.FILES, instance=datapimpinan)
        if form.is_valid:
            form.save() 
    context = {
        'menu': 'Profil Kepala Sekolah',
        'page' : 'Halaman Profil',
        'formpimpinan': form
    }
    return render(request, 'inventaris/pimpinan/profil_pimpinan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def data_inventaris(request):
    data = Barang.objects.order_by('-kode_barang')
    list_barang = Barang.objects.all()
    # filter_barang = BarangFilter(request.GET, queryset=list_barang)
    # list_barang = filter_barang.qs 
    halaman_tampil = Paginator(list_barang, 3)
    halaman_url = request.GET.get('halaman', 1)
    halaman_barang = halaman_tampil.get_page(halaman_url)
    
    if halaman_barang.has_previous():
        url_previous = f'?halaman={halaman_barang.previous_page_number()}'
    else:
        url_previous = ''
            
    if halaman_barang.has_next():
        url_next = f'?halaman={halaman_barang.next_page_number()}'
    else:
        url_next = ''
    context = {
        "menu" : 'Data Inventaris',
        "page" : 'Data Inventaris',
        'barang' : data,
        # 'obj' : obj,
        # 'filter_data_barang' : filter_barang,
        'halaman_list_barang' : halaman_barang,
        'previous' : url_previous,
        'next' : url_next,

    }
    return render(request, 'inventaris/pimpinan/inventaris.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def qrcode(request, pk):
    obj = Barang.objects.get(id=pk)
    kode_barang = "kode_barang"

    context = {
        "menu" : 'Cetak QR Code',
        "page" : 'Halaman Cetak QR Code',
        'obj' : obj,
        'kode_barang' : kode_barang,
    }
    return render(request, 'inventaris/pimpinan/qrcode.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def ruangan(request):
    dt_ruangan = Ruangan.objects.order_by('-kode_ruangan')
    context = {
        'menu' : 'Data Ruangan',
        'page' : 'Halaman Data Ruangan',
        'ruangan' : dt_ruangan
    }
    return render(request, 'inventaris/pimpinan/ruangan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def dtpengecekan(request):
    context = {
    "menu" : 'Pengecekan Inventaris',
    "page" : 'Data Pengecekan Inventaris', 
    }
    return render(request, 'inventaris/pimpinan/dtpengecekan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def dtperpindahan(request):

   

    context = {
    "menu" : 'Perpindahan Inventaris',
    "page" : 'Data Perpindahan Inventaris'  
    

    }
    return render(request, 'inventaris/pimpinan/dtperpindahan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def dtpeminjaman(request):
    context = {
    "menu" : 'Peminjaman Inventaris',
    "page" : 'Data Peminjaman Inventaris'  
    }
    return render(request, 'inventaris/pimpinan/dtpeminjaman.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def dtpengembalian(request):
    context = {
    "menu" : 'Pengembalian Inventaris',
    "page" : 'Data Pengembalian Inventaris'  
    }
    return render(request, 'inventaris/pimpinan/dtpengembalian.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def profil(request):
    datapetugas = request.user.petugas
    form = PetugasForm(instance = datapetugas)
    if request.method == 'POST':
        form = PetugasForm(request.POST, request.FILES, instance=datapetugas)
        if form.is_valid:
            form.save() 
    context = {
        'menu': 'Profil',
        'page' : 'Halaman Profil',
        'formpetugas': form
    }
    return render(request, 'inventaris/profil.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['pimpinan'])
def dtpetugas(request):
    dt_petugas = Petugas.objects.all()
    context = {
        'menu' : 'Data Pengguna',
        'page' : 'Halaman Data Pengguna',
        'petugas' : dt_petugas
    }
    return render(request, 'inventaris/pimpinan/dtpetugas.html', context)

@tolakhalaman_ini
def loginPage(request):
    formlogin = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        status = request.POST.get('status')

        cocok = authenticate(request, username=username, password=password)
        if cocok is not None:
            login(request, cocok)
            return redirect('beranda')

        else:
            return redirect('login')

        # else:
        #     messages.error(request, 'Nama pengguna atau Kata sandi salah')
        #     return redirect('login')

        # if User.objects.filter(username = username).first():
        #     messages.success(request, 'Username tidak tersedia')
        #     return redirect('login')

        # else:
        #     messages.success(request, 'Password salah')
        #     return redirect('login')

    context = {
        "menu" : 'Halaman Login',
        "page" : 'login',
        'tampillogin' : formlogin    

    }
    return render(request, 'inventaris/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


#Penambahan View REST API

class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        user = User.objects.filter(username = request.data.get('username')).first()
        if user is None:
            return Response({'message': 'No user found', 'status':False, 'data' : {}})

        serializer = self.serializer_class(data = request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user = user)
            # return Response({'message': 'Success', 'status':True, 'data':{
            return Response({
                'id': user.id,
              
                'username':user.username,
                'token':token.key,
                'password': user.password
            })
        return Response({'message':'Login failed', 'status':False, 'data':{}})

class RegisterViewSet(viewsets.ViewSet):
    serializer_class = UserAccountSerializer

    def create(self, request):
        serializer = UserAccountSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            user = Petugas(email = serializer.data.get('email'),
                               name = serializer.data.get('name'))
            user.set_password(request.data.get('password'))
            user.save()
            return Response({'message': 'Success', 'status':True, 'data':serializer.data})



class BarangViewSet(FlexFieldsModelViewSet):
    # Barang = Barang.objects.filter(id=pk).first()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BarangSerializer
    queryset = Barang.objects.all()

    def create(self, request):
        serializer = BarangSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            lokasi = Ruangan.objects.filter(nama_ruangan = request.data.get('lokasi')).first()
            
            # statusbarang = Status.objects.filter(id = request.data.get('status')).first()
            barangkirim = PindahBarang.objects.filter(kode_barang = request.data.get('PindahBarang')).first()
          
            PindahBarang.kode_barang_id = request.POST.get('kode_barang_id')
            #  barangs = Barang.objects.filter(kode_barang = request.data.get('barang')).first()
            # ruang = Ruangan.objects.filter(name = request.data.get('lokasi')).first()
            # barangs.lokasi_id = '1' 
            databarang = Barang(nama_barang=serializer.data.get('nama_barang'),
                        keterangan = serializer.data.get('keterangan'),
                        kode_barang =serializer.data.get('kode_barang'),
                        kategori_barang =serializer.data.get('kategori_barang'),
                        jenis_barang = serializer.data.get('jenis_barang'),
                        status = serializer.data.get('status'),
                        kondisi_barang = serializer.data.get('kondisi_barang'),
                        gambar = request.FILES['gambar'],
                        # qrcode = request.FILES['qrcode'],
                        lokasi = lokasi,
                        
                       
                        # status = statusbarang,
                     )
            databarang.save()
           
            kirimlokasi = PindahBarang(kode_barang_id = databarang.id,
                                        lokasi = lokasi)
            
            kirimlokasi.save()       
            return Response({'message': 'Success', 'status': True, 'data': serializer.data})

    def retrieve(self, request, pk = None):
        # id = Barang.objects.filter(id = pk).first()
        product = Barang.objects.filter(kode_barang = pk).first()
        serializer = BarangSerializer(product, many=True)
        if product is None:
            return Response({'message': 'Data not found', 'status': False, 'data': {}})
        else:
            serializer = BarangSerializer(product, many=False)
            return Response( serializer.data)

    def partial_update(self, request, pk = None):
            # Barang = Barang.objects.filter(id = pk).first()
            product = Barang.objects.filter(kode_barang = pk).first()
            if product is None:
                return Response({'message': 'Data not found', 'status': False, 'data': {}})
            else:
                serializer = BarangDescriptiveSerializer(product, data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({'message': 'Success', 'status': True, 'data': serializer.data})

   
class RoomViewSet(FlexFieldsModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = RoomSerializer
    queryset = Ruangan.objects.all()


        # def list(self, request):
        #     # cat = Category.objects.filter(id = request.data.get('category')).first()

        #     # room = Ruangan.objects.select_related('nama_ruangan').filter(nama_ruangan = request.data.get('nama_ruangan'))
        #     # room = Ruangan.objects.select_related(id = request.data.get('id')).first()
        #     serializer = RoomSerializer(room, many=True)
        #     return Response({'message': 'Success', 'status': True, 'data': serializer.data})

    def retrieve(self, request, pk = None):
        # id = Barang.objects.filter(id = pk).first()
        room = Ruangan.objects.filter(id = pk).first()
        serializer = BarangSerializer(room, many=True)
        if room is None:
            return Response({'message': 'Data not found', 'status': False, 'data': {}})
        # if Barang is None:
        #     return Response({'message': 'Data not found', 'status': False, 'data': {}})
        else:
            serializer = RoomDescriptiveSerializer(room, many=False)
            return Response(serializer.data)

    def create(self, request):
        serializer = RoomDescriptiveSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            users = User.objects.filter(id = request.data.get('user')).first()
            room = Ruangan(nama_ruangan=serializer.data.get('nama_ruangan'),
                    
                        keterangan=serializer.data.get('keterangan'),
                        kode_ruangan =serializer.data.get('kode_ruangan'),
                        user = users
                        # image = request.FILES['image']
                        # qrcode = request.FILES['qrcode'],
                     )
                        # status = serializer.data.get('status'),
                        # kode_barang = serializer.data.get('kode_barang'),
                        # category=cat)

            room.save()
            return Response({'message': 'Success', 'status': True, 'data': serializer.data})

    def partial_update(self, request, pk = None):
        room = Ruangan.objects.filter(name = pk).first()
        if room is None:
            return Response({'message': 'Data not found', 'status': False, 'data': {}})
        else:
            serializer = RoomDescriptiveSerializer(room, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': 'Success', 'status': True, 'data': serializer.data})

    def destroy(self, request, pk = None):
        room = Ruangan.objects.filter(id = pk).first()
        if room is None:
            return Response({'message': 'Data not found', 'status': False, 'data': {}})
        else:
            room.delete()
            return Response({'message': 'Success', 'status': True, 'data': {}})


class PindahViewSet(FlexFieldsModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = PindahSerializer
    queryset = PindahBarang.objects.all()

    def create(self, request, pk = None):
        serializer = PindahSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            
            barangs = Barang.objects.filter(kode_barang = request.data.get('kode_barang')).first()
            ruang = Ruangan.objects.filter(nama_ruangan = request.data.get('lokasi')).first()
            cek = PindahBarang(kode_barang = barangs,
            lokasi = ruang)
            cek.save()
            
            barangs.lokasi_id = ruang
            barangs.save()
           

            return Response({'message': 'Success', 'status':True, 'data':serializer.data})

# class StatusViewSet(FlexFieldsModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     serializer_class = StatusSerializer
#     queryset = Status.objects.all()

#     def create(self, request, pk = None):
#         serializer = StatusSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
            
#             # barangs = Barang.objects.filter(id = request.data.get('kode_barang')).first()
#             # ruang = Ruangan.objects.filter(name = request.data.get('lokasi')).first()
#             status = Status(namastatus = serializer.data.get('namastatus'),
#                         keterangan = serializer.data.get('keterangan'))
#             status.save()
            
#             # barangs.lokasi_id = ruang
#             # barangs.save()
           

#             return Response({'message': 'Success', 'status':True, 'data':serializer.data})


class InvViewSet(FlexFieldsModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = InvSerializer
    queryset = Inventaris.objects.all()


    def create(self, request, pk = None):
        serializer = InvSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            
            barangs = Barang.objects.filter(kode_barang = request.data.get('barang')).first()
            # ruang = Ruangan.objects.filter(name = request.data.get('lokasi')).first()
            cek = Inventaris(nama = serializer.data.get('nama'),
                                status = serializer.data.get('status'),
                                tanggalkembali = serializer.data.get('tanggalkembali'),
            barang = barangs)
            cek.save()
            
            #   kirimlokasi = PindahBarang(kode_barang_id = databarang.id,
            #                             lokasi = lokasi)
            
            # kirimlokasi.save()     

            # barangs.statusbarang = cek.status
            barangs.status = cek.status
            barangs.save()
           

            return Response({'message': 'Success', 'status':True, 'data':serializer.data})


