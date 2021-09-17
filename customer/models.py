from django.db import models

# Create your models here.

class Customer_details(models.Model):
    customer_name=models.CharField(max_length=20)
    mobile_number=models.CharField(max_length=11)
    address=models.CharField(max_length=50)
    state=models.CharField(max_length=10)
    city=models.CharField(max_length=10)
    email=models.EmailField()
    payment_detail=models.IntegerField()



# class Hotel_booking(models.Model):
#     customer_name=models.CharField(max_length=20)
#     customer_age=models.IntegerField()
#     email=models.EmailField()
#     phone_number=models.CharField(max_length=20)
#     appointment_date=models.DateField()
#     state=models.CharField(max_length=10)
#     city=models.CharField(max_length=10)    