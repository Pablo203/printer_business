# Generated by Django 3.2.16 on 2022-12-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_categoryvalue_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryvalue',
            name='data',
            field=models.JSONField(default=dict),
        ),
    ]
