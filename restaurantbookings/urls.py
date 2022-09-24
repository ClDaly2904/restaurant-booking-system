from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookingView.as_view(), name='BookTable'),
    path('menu/', views.GetMenu.as_view(), name='menu'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('mybookings/', views.UserBookings.as_view(), name='mybookings'),
    path('editbooking/<booking_id>', views.edit_booking, name='editbooking')
]
