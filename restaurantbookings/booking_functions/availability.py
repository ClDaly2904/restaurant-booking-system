""" This file contains the availability logic for the booking functionality """
from restaurantbookings.models import Booking, Table


def check_availability(booking_date_time_start, booking_date_time_end, people):
    """ Takes user input from availability form, checks size of each table and
    makes sure table does not already have a booking for that time frame,
    returns a list of available tables """

    # create empty list to hold available tables
    avail_list = []

    # check every table to ensure it has enough seats for the guests
    big_enough_tables = Table.objects.filter(no_seats__gte=people)

    # create empty list to hold existing bookings
    existing_bookings = []

    # iterate through existing bookinds to see if any are within the
    # same time frame, and if they are then add them to the existing bookings list
    bookings = Booking.objects.all()
    for booking in bookings:
        if booking.booking_date_time_start <= booking_date_time_end or booking.booking_date_time_end >= booking_date_time_start:
            existing_bookings.append(booking)

    # get a list of the table numbers in the existing bookings
    booked_tables = Table.objects.filter(booking__in=existing_bookings)

    # iterate through all table objects to see which are big enough and not alread booked
    tables = Table.objects.all()
    for table in tables:
        if table in big_enough_tables and table not in booked_tables:
            avail_list.append(table)

    # return a list of all available tables
    return (avail_list)
