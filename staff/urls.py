from staff.forms import Login_form
from django.urls import path
from . import views
from customer.forms import Customer_form
from customer.views import Customer_form,Details,Hotel_booking

urlpatterns=[
    path('',views.Home.as_view(),name="home"),
    path('login',views.Login_forms.as_view(),name='login_forms'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('add_customer',Customer_form.as_view(),name='add_customer'),
    path('details/',Details.as_view(),name="details"),
    path('booking',Hotel_booking.as_view(),name='booking'),
    path('views_appointment',Details.as_view(),name='details')
]