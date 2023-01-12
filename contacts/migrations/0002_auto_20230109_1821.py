# Generated by Django 3.2.16 on 2023-01-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='photoPath',
            field=models.CharField(default='/static/contacts/no-image.png', max_length=100),
        ),
    ]