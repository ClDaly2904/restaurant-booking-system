import datetime
from restaurantbookings.models import Table, Booking


def check_availability(table, booking_date_time_start, booking_date_time_end):
    avail_list = []
    booking_list = Booking.objects.filter(table=table)
    for booking in booking_list:
        if booking.booking_date_time_start > booking_date_time_end or booking.booking_date_time_end < booking_date_time_start:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
