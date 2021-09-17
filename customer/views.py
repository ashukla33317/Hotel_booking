from staff import views
from django.shortcuts import redirect, render
from django.views import View
from . import forms
from . import models
# Create your views here.

class Customer_form(View):
    def get(self,request):
        content={
            'add_customer':forms.Customer_form(),
            'customer_details':models.Customer_details.objects.all()
        }
        return render(request,'add_customer.html',content)

    def post(self,request):
            customer_name=request.POST['customer_name']
            mobile_number=request.POST['mobile_number']
            address=request.POST['address']
            state=request.POST['state']
            city=request.POST['city']
            email=request.POST['email']
            # check_in_date=request.POST['check_in_date']
            # check_out_date=request.POST['check_out_date']
            payment_detail=request.POST['payment_detail']
            new_details=models.Customer_details(
                customer_name=customer_name,
                mobile_number= mobile_number,
                address= address,
                state=state,
                city=city,
                email=email,
                payment_detail=payment_detail
            )
            new_details.save()
            print(new_details)
            return redirect('/')    

class Details(View):
    def get(self,request):
        # customer_id = request.GET['customer_id']
        content={
            'customer_details':models.Customer_details.objects.all()
        }
        return render(request,'update_info.html',content)

class Hotel_booking(View):
    def get(self,request):
        content={
            'hotel_booking':forms.Hotel_book()
        }
        return render(request,'hotel_booking.html',content)

    def post(self,request):
        customer_name=request.POST['customer_name']
        phone_number=request.POST['phone_number']
        customer_age=request.POST['customer_age']
        state=request.POST['state']
        email=request.POST['email']
        city=request.POST['city']
        appointment_date=request.POST['appointment_date']
        book_hotel=models.Hotel_booking(
        customer_name=customer_name,
        phone_number=phone_number,
        state=state,
        email=email,
        city=city,
        customer_age=customer_age,
        appointment_date=appointment_date
        )

        book_hotel.save()
        return redirect('/')