from django.db.models import fields
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import *
from versatileimagefield.serializers import VersatileImageFieldSerializer


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password' : { 'write_only': True }}


# class NoteDescriptiveSerializer(serializers.ModelSerializer):
#     status = Status(many=False, read_only=True)

#     class Meta:
#         model = Note
#         fields = '__all__'
#         extra_kwargs = {'status': {'read_only':True}, 'user': {'read_only':True}}

# class StatusDescriptiveSerializer(FlexFieldsModelSerializer):
#     # barang = BarangDescriptiveSerializer(many=False, read_only=True)
#     class Meta:
#         model = Status
#         fields = '__all__'
#         extra_kwargs = {'status': {'read_only':True}, 'user': {'read_only':True}}



class RoomDescriptiveSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Ruangan
        fields = '__all__'
        # fields = ['pk', 'name', 'image','user','category','description']
        # extra_kwargs = {'category': {'read_only':True}, 'user': {'read_only':True}}
        extra_kwargs = {'user': {'read_only':True}}

class BarangDescriptiveSerializer(serializers.ModelSerializer):
    # room = RoomDescriptiveSerializer(many=False, read_only=True)
    # status = StatusDescriptiveSerializer(many = False, read_only=True)
    class Meta:
        model = Barang
        fields = '__all__'
        # fields = ['name', 'description', 'image', 'qrcode', 'category', 'kode_barang','image_ppoi']
        extra_kwargs = {'status': {'read_only':True}, 'user': {'read_only':True}}


class BarangSerializer(serializers.ModelSerializer):
    # room = RoomDescriptiveSerializer(many=False, read_only=True)
    lokasi = RoomDescriptiveSerializer(many=False, read_only=True)
    # status = StatusDescriptiveSerializer(many = False, read_only=True)
    # categories = GoodsCategory.objects.filter(name=category_name)
    
    # image = VersatileImageFieldSerializer(
    #     sizes='Barang_headshot'
    # )

    class Meta:
        model = Barang
        fields = '__all__'
        # fields = ['pk', 'name', 'image','user','category','description']

class CekDescriptiveSerializer(FlexFieldsModelSerializer):
    # barang = BarangDescriptiveSerializer(many=False, read_only=True)
    class Meta:
        model = CekBarang
        fields = '__all__'
        extra_kwargs = {'status': {'read_only':True}, 'user': {'read_only':True}}

class CekSerializer(serializers.ModelSerializer):
    barang = BarangDescriptiveSerializer(many=False, read_only=True)
    # lokasi = RoomDescriptiveSerializer(many=False, read_only=True)
    
    class Meta:
        model = CekBarang
        fields = '__all__'
        extra_kwargs = {'user': {'read_only':True}}

class PindahDescriptiveSerializer(FlexFieldsModelSerializer):
    barang = BarangDescriptiveSerializer(many=False, read_only=True)
    class Meta:
        model = PindahBarang
        fields = '__all__'
        extra_kwargs = {'status': {'read_only':True}, 'user': {'read_only':True}}


class RoomSerializer(FlexFieldsModelSerializer):
    # category = CategoryPlainSerializer(many=False, read_only=True)
    # categories = GoodsCategory.objects.filter(name=category_name)
    
    # image = VersatileImageFieldSerializer(
    #     sizes='Barang_headshot'
    # )

    class Meta:
        model = Ruangan
        fields = '__all__'
        # fields = ['pk', 'name', 'image','user','category','description']

# class StatusSerializer(FlexFieldsModelSerializer):

#     class Meta:
#         model  = Status
#         fields = '__all__'
        
class PindahSerializer(serializers.ModelSerializer):
    kode_barang = BarangDescriptiveSerializer(many=False, read_only=True)
    lokasi = RoomDescriptiveSerializer(many=False, read_only=True)

    class Meta:
        model = PindahBarang
        fields = '__all__'
        # extra_kwargs = {'user': {'read_only':True}}


# class StatusDescriptiveSerializer(serializers.ModelSerializer):
#     # note = NoteDescriptiveSerializer(many=True, read_only=True)
#     Barang = BarangDescriptiveSerializer(many=True, read_only=True)
#     room = RoomDescriptiveSerializer(many=True, read_only=True)
#     class Meta:
#         model = Status
#         fields = '__all__'

        
class InvDescriptiveSerializer(FlexFieldsModelSerializer):
    # barang = BarangDescriptiveSerializer(many=False, read_only=True)
    class Meta:
        model = Inventaris
        fields = '__all__'
        extra_kwargs = {'status': {'read_only':True}, 'user': {'read_only':True}}

class InvSerializer(serializers.ModelSerializer):
    barang = BarangDescriptiveSerializer(many=False, read_only=True)
    # lokasi = RoomDescriptiveSerializer(many=False, read_only=True)
    
    class Meta:
        model = Inventaris
        fields = '__all__'
        extra_kwargs = {'user': {'read_only':True}}

