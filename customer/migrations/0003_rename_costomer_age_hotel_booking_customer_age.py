# Generated by Django 3.2.6 on 2021-09-17 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_hotel_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel_booking',
            old_name='costomer_age',
            new_name='customer_age',
        ),
    ]