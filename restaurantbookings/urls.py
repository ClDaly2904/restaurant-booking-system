from django.urls import path
from . import views

urlpatterns = [
    path('booking_list/', views.BookingList.as_view(), name='BookingList'),
    path('book/', views.BookingView.as_view(), name='BookTable'),
    path('menu/', views.GetMenu.as_view(), name='menu'),
    path('contact/', views.ContactView.as_view(), name='contact')
]
