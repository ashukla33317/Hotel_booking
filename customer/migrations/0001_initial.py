# Generated by Django 3.2.6 on 2021-09-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('payment_detail', models.IntegerField()),
            ],
        ),
    ]
