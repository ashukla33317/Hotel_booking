from staff import views
from django.shortcuts import redirect, render
from django.views import View
from . import forms
from . import models
import customer

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
        customer_id = request.GET['customer_id']
        content={
            'customer_details':models.Customer_details.objects.get(id=customer_id)
        }
        return render(request,'update_info.html',content)
