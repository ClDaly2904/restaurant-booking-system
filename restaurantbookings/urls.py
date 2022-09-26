from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookingView.as_view(), name='BookTable'),
    path('menu/', views.GetMenu.as_view(), name='menu'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('mybookings/', views.UserBookings.as_view(), name='mybookings'),
    path('editbooking/<booking_id>/', views.EditBooking.as_view(), name='editbooking'),
    path('deletebooking/<booking_id>/', views.delete_booking, name='deletebooking'),
]
