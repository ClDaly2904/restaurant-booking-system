""" Contains URL paths for the restaurant bookings app,
forming part of the main Sushi & Sake website """
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookingView.as_view(), name='BookTable'),
    path('mybookings/', views.UserBookings.as_view(), name='mybookings'),
    path('editbooking/<booking_id>/', views.EditBooking.as_view(),
         name='editbooking'),
    path('confirmdelete/<booking_id>/', views.ConfirmDelete.as_view(),
         name='confirmdelete'),
]
