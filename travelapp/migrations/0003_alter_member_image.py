# Generated by Django 4.1 on 2022-08-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_destination_price_from_alter_destination_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(upload_to='members'),
        ),
    ]