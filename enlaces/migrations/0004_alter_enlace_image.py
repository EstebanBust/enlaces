# Generated by Django 4.2 on 2023-04-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enlaces', '0003_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enlace',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
