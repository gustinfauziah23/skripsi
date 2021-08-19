from django.db import models
import qrcode 
from io import BytesIO
from django.core.files import File 
from PIL import Image, ImageDraw 
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from datetime import datetime
from django.db.models.deletion import CASCADE
#
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.conf import settings


#untuk REST_API (ANDROID)
class UserAccountManager(BaseUserManager):
    def create_user(self,email, name, password = None):
        if not email:
            raise ValueError("User must have an email address")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save(using = self._db)
        return user

    # def create_superuser(self, email, name, password):
    #     email = self.normalize_email(email)
    #     user = self.model(email = email, name = name)
    #     user.set_password(password)
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.save(using = self._db)
    #     return user


# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255, blank=False, null=False)
#     password = models.CharField(max_length=255, validators=[MinLengthValidator(8)])
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     objects = UserAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         return self.name

#     def __str__(self):
#         return "{0} - {1}".format(self.name, self.email)


##

# Create your models here.
class Petugas(models.Model):
    Status = (
        ('Admin', 'Admin'),
        ('Kepala Sekolah', 'Kepala Sekolah' ),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # id_petugas = models.IntegerField(unique=True, null=True)
    nama = models.CharField(max_length=30)
    nip = models.CharField(max_length=18)
    tempat_tanggal_lahir = models.CharField(max_length=50)
    pendidikan = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    alamat = models.CharField(max_length=50)
    no_hp = models.CharField(max_length=12)
    status = models.CharField(max_length=30, blank=True, null=True, choices=Status)
    foto = models.ImageField(default='fotokosong.jpg', blank=True)

    def __str__(self):
        return '%s' % (self.nama)
    class Meta:
        verbose_name_plural = "Petugas"

    def save(self, *args, **kwargs):
        super(Petugas, self).save(*args, **kwargs)

        img = Image.open(self.foto.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.foto.path)

class Ruangan(models.Model):
    kode_ruangan = models.CharField(max_length=50)
    nama_ruangan = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
       return '%s' % (self.nama_ruangan)
    
    class Meta:
       verbose_name_plural = "Ruangan"

class Barang(models.Model):
  
    Kondisi = (
        ('Baik', 'Baik'),
        ('Rusak', 'Rusak'),
    )
    JenisBarang = (
        ('Barang Masuk', 'Barang Masuk'),
        ('Barang Keluar', 'Barang Keluar'),
       
    )
    Kategori = (
        ('Barang Habis Pakai', 'Barang Habis Pakai'),
        ('Barang Tidak Habis Pakai', 'Barang Tidak Habis Pakai'),
    )
    Status = (
        ('Di Pinjam', 'Di Pinjam'),
        ('Di Kembalikan', 'Di Kembalikan'),
     

    )
    kode_barang = models.CharField(max_length=20, blank=True, null=False)
    nama_barang = models.CharField(max_length=20, blank=True, null=False)
    # nama= models.CharField(max_length=15, blank=True, null=True)
    kondisi_barang = models.CharField(max_length=30, blank=True, null=True, choices=Kondisi)
    lokasi = models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    jenis_barang = models.CharField(max_length=30, blank=True, null=True, choices=JenisBarang)
    kategori_barang = models.CharField(max_length=30, blank=True, null=True, choices=Kategori)
    tanggal = models.CharField(max_length=20, blank=True, null=True)
    tgl_update = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True, choices=Status)
    keterangan = models.CharField(max_length=50, blank=True, null=True)
    gambar = models.ImageField(upload_to='foto')
    qrcode = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return '%s' % (self.kode_barang)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.kode_barang)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qrcode-{self.kode_barang}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcode.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs) 
    
    class Meta:
       verbose_name_plural = "Barang"

class CekBarang (models.Model):
    kode_barang = models.ForeignKey(Barang, on_delete=models.CASCADE, null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.barang

    class Meta:
        verbose_name_plural = "CekBarang"

class PindahBarang(models.Model):
    kode_barang = models.ForeignKey(Barang, on_delete=CASCADE, related_name='barangcapek')
    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
    lokasi = models.ForeignKey(
        Ruangan,
        on_delete=models.CASCADE,
        related_name="lokasi",
    )
    tanggal = DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s' % (self.kode_barang)

    class Meta:
        verbose_name_plural = "PindahBarang"

    

class Inventaris(models.Model):
    Status = (
        ('Di Pinjam', 'Di Pinjam'),
        ('Di Kembalikan', 'Di Kembalikan')
        # ('Di Cek', 'Di Cek'),
        # ('Di Pindah', 'Di Pindah')
    )
    barang = models.ForeignKey(Barang, on_delete=CASCADE, related_name='inventaris')
    nama = models.CharField(max_length=50) 
    status = models.CharField(max_length=150, null=True, blank=True, choices=Status)
    tanggalpinjam  = models.DateField(default=datetime.now)
    tanggalkembali = models.DateField(default=datetime.now)

    def __str__(self):
       return '%s' % (self.barang)

  
