# Generated by Django 3.2.6 on 2021-08-18 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventaris', '0003_alter_ruangan_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='lokasi_barang',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventaris.ruangan'),
            preserve_default=False,
        ),
    ]
