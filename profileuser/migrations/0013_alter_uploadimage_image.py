# Generated by Django 4.1 on 2022-11-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileuser', '0012_alter_uploadimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(default='images/profiledefault.jpg', upload_to='images'),
        ),
    ]
