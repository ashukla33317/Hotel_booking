from staff.forms import Login_form
from django.urls import path
from . import views
from customer.forms import Customer_form
from customer.views import Customer_form,Details

urlpatterns=[
    path('',views.Home.as_view(),name="home"),
    path('add_customer',Customer_form.as_view(),name='add'),
    path('login',views.Login_forms.as_view(),name='login_forms'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('details/',Details.as_view(),name="details"),
    # path('booking',Hotel_booking.as_view(),name='booking'),
    path('views_appointment',views.Display.as_view(),name='details')
]