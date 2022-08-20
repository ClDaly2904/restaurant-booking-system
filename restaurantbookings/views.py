from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Table, Booking
from .forms import AvailabilityForm
from .booking_functions.availability import check_availability


# Create your views here.


class TableList(ListView):
    model = Table


class BookingList(ListView):
    model = Booking


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(location=data['table_location'])

        available_tables = []
        
        for table in table_list:
            if check_availability(table, data['booking_date_time_start'], data['booking_date_time_end']):
                available_tables.append(table)
        
        room = available_tables[0]
        booking = Booking.objects.create(
            user = request.user
        )
