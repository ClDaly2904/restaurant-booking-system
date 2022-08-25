from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from restaurantbookings.booking_functions.availability import check_availability
from .models import Table, Booking
from .forms import AvailabilityForm


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
        people = data['people']

        for table in table_list:
            if check_availability(table, data['booking_date_time_start'], data['booking_date_time_end']):
                # check table is big enough for number of people
                if table.no_seats >= people:
                    available_tables.append(table)

        if len(available_tables) > 0:
            table = available_tables[0]
            booking = Booking.objects.create(
                guest=self.request.user,
                table=table,
                people=data['people'],
                booking_date_time_start=data['booking_date_time_start'],
                booking_date_time_end=data['booking_date_time_end']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This table type is fully booked')


def get_homepage(request):
    return render(request, 'sushisake/index.html')
