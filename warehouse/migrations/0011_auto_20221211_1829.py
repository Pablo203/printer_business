# Generated by Django 3.2.16 on 2022-12-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0010_position_imagepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryvalue',
            name='propertyValue',
        ),
        migrations.AlterField(
            model_name='position',
            name='imagePath',
            field=models.CharField(default='/static/positionImgs/no-product-image.png', max_length=200),
        ),
    ]
