# Generated by Django 3.2.16 on 2022-12-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0009_auto_20221203_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='imagePath',
            field=models.CharField(default='/home/a4ch3r/Documents/printer_business/static/dist/img/no-product-image.png', max_length=200),
        ),
    ]