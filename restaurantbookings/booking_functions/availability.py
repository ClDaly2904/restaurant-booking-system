import datetime
from restaurantbookings.models import Table, Booking


def check_availability(table, booking_date_time_start, booking_date_time_end):

    # create empty list
    avail_list = []

    booking_list = Booking.objects.filter(table=table)

    for booking in booking_list:
        # check for tables available in booking request timeframe
        if booking.booking_date_time_start > booking_date_time_end or booking.booking_date_time_end < booking_date_time_start:
            avail_list.append(True)
            return avail_list
        else:
            avail_list.append(False)

    return all(avail_list)
