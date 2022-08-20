from django.urls import path
from .views import TableList, BookingList, BookingView

app_name = 'restaurantbookings'

urlpatterns = [
    path('table_list/', TableList.as_view(), name='TableList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view')
]