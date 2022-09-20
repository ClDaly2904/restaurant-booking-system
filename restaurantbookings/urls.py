from django.urls import path
from .views import TableList, BookingList, BookingView, get_homepage, GetMenu, ContactView

app_name = 'restaurantbookings'

urlpatterns = [
    path('table_list/', TableList.as_view(), name='TableList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookTable'),
    path('', get_homepage, name='home'),
    path('menu/', GetMenu.as_view(), name='menu'),
    path('contact/', ContactView.as_view(), name='contact')
]
