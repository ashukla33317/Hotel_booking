from django import forms
from django.forms.fields import EmailField


class Customer_form(forms.Form):
    customer_name=forms.CharField(max_length=20)
    mobile_number=forms.CharField(max_length=11)
    address=forms.CharField(max_length=50)
    state=forms.CharField(max_length=10)
    city=forms.CharField(max_length=10)
    email=forms.EmailField()
    payment_detail=forms.IntegerField()



class Hotel_book(forms.Form):
    customer_name=forms.CharField(max_length=20)
    phone_number=forms.IntegerField()
    customer_age=forms.IntegerField()
    email=forms.EmailField()
    state=forms.CharField(max_length=10)
    city=forms.CharField(max_length=10)
    appointment_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
