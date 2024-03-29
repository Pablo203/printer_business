# Generated by Django 3.2.16 on 2023-01-09 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20230109_1821'),
        ('warehouse', '0012_position_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='imagePath',
            field=models.CharField(default='/static/positionImgs/no-image.png', max_length=200),
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.position')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact')),
            ],
        ),
    ]
