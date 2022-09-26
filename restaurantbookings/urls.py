from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookingView.as_view(), name='BookTable'),
    path('menu/', views.GetMenu.as_view(), name='menu'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('mybookings/', views.UserBookings.as_view(), name='mybookings'),
    path('editbooking/<booking_id>/', views.EditBooking.as_view(), name='editbooking'),
    path('confirmdelete/<booking_id>/', views.ConfirmDelete.as_view(), name='confirmdelete'),
    path('admindashboard/', views.AdminDashboard.as_view(), name='admin_dashboard'),
]
