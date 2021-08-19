from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PetugasForm(ModelForm):
    class Meta :
        model = Petugas
        fields= '__all__'
        exclude = ['user']

        widgets = {
            'nama' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama lengkap'}),
            'nip' : forms.TextInput(attrs={'class': 'form-control', 'type' : 'number', 'placeholder': 'Masukkan NIP'}),
            'tempat_tanggal_lahir' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan tempat dan tanggal lahir'}), 
            'pendidikan' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan pendidikan'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Masukkan email'}),
            'alamat' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan alamat'}),
            'no_hp' : forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Masukkan no hp'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            'nama' : 'Nama Lengkap',
            'nip' : 'NIP',
            'tempat_tanggal_lahir' : 'Tempat, Tanggal Lahir',
            'pendidikan' : 'Pendidikan',
            'email' : 'Email',
            'alamat' : 'Alamat',
            'no_hp' : 'No Hp',
            'status' : 'Status',
        }


class RuanganForm(ModelForm):
    class Meta:
        model = Ruangan
        fields = ['kode_ruangan', 'nama_ruangan', 'keterangan']

        widgets = {
           'kode_ruangan' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan kode ruangan'}),
           'nama_ruangan' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama ruangan'}),
           'keterangan' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keterangan'}),
        }
        labels = {
           'kode_ruangan' : 'Kode Ruangan',
           'nama_ruangan' : 'Nama Ruangan',
           'keterangan' : 'Keterangan',
        }

class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'
        exclude = ['nama', 'qrcode']

        widgets = {
            'kode_barang' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan kode barang'}),
            'nama_barang' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama barang'}),
            'kondisi_barang' : forms.Select(attrs={'class': 'form-control'}),
            'lokasi' : forms.Select(attrs={'class': 'form-control'}),
            'jenis_barang' : forms.Select(attrs={'class': 'form-control'}),
            'kategori_barang' : forms.Select(attrs={'class': 'form-control'}),
            'tanggal' : forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control', 'placeholder': 'Masukkan tanggal'}),
            'tgl_update' : forms.DateInput(attrs={'class': 'form-control', 'type': 'month'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
            'keterangan' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keterangan barang'}),
        }
        labels = {
            'kode_barang' : 'Kode Barang',
            'nama_barang' : 'Nama Barang',
            'kondisi_barang' : 'Kondisi',
            'lokasi' : 'Lokasi',
            'jenis_barang' : 'Jenis Barang',
            'kategori_barang' : 'Kategori',
            'tanggal' : 'Tanggal',
            'tgl_update' : 'Tanggal Update',
            'status' : 'Status Barang',
            'keterangan' : 'Keterangan',

        }

  
