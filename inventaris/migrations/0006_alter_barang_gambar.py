# Generated by Django 3.2.6 on 2021-08-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaris', '0005_rename_lokasi_barang_barang_lokasi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='gambar',
            field=models.ImageField(upload_to='foto'),
        ),
    ]