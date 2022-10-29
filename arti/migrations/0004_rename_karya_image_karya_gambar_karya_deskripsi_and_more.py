# Generated by Django 4.1 on 2022-10-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arti', '0003_karya_harga'),
    ]

    operations = [
        migrations.RenameField(
            model_name='karya',
            old_name='karya_image',
            new_name='gambar',
        ),
        migrations.AddField(
            model_name='karya',
            name='deskripsi',
            field=models.CharField(default='nonononon', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='karya',
            name='judul',
            field=models.CharField(default='ononoonnono', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='karya',
            name='harga',
            field=models.CharField(max_length=255),
        ),
    ]