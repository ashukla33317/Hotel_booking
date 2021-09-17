from django.shortcuts import redirect, render
from django.views import  View
from customer import forms, models
from customer.forms import Customer_form
from customer.models import Customer_details
from django.contrib.auth.models import auth,User
# from django .contrib import auth
from .import forms
# Create your views here.
class Home(View):
    def get(self,request):
        content={
            'page_title':'Hotel_booking_system',
            'add_customer':Customer_form(),
            'customer_details':Customer_details.objects.all()

        }
        return render(request,'index.html',content)


class Login_forms(View):
    def get(self,request):
        content={
            'login_forms':forms.Login_form
        }
        return render(request,'login.html',content)

    def post(self,request):
        user_name=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            print('authentication is successfully ')
            auth.login(request,user)
        return redirect('/')    


class Display(View):
    def get(self,request):
        if request.user.is_authenticated:
            content={
                'hotel_booking':Customer_details.objects.all()
            }
            page='display_page.html'
            return render(request,page,content)
        else:
            page='404.html'
            return render(request,page)   

class Logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')        
