# Generated by Django 3.2.16 on 2023-01-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20230109_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photoPath',
            field=models.CharField(default='/static/contacts/no-user-photo.png', max_length=100),
        ),
    ]
