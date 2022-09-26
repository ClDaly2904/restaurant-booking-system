from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView, View
from django.contrib import messages
from restaurantbookings.booking_functions.availability import check_availability
from .models import Table, Booking, FoodItem
from .forms import AvailabilityForm, ContactForm


# Create your views here.


class TableList(ListView):
    model = Table


class BookingList(ListView):
    model = Booking


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'sushisake/availability_form.html'

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
            messages.success(self.request, 'Your booking has been successful! \n'
                                        f'Your table has been booked from {booking.booking_date_time_start}\n'
                                        f' to {booking.booking_date_time_end}')
            return HttpResponseRedirect(reverse('sushisake'))
        else:
            messages.error(self.request, 'Sorry, the table type for this time is full, please try again. ')
            return HttpResponseRedirect(reverse('BookingTable'))


class get_homepage(View):
    def get(self, request):
        return render(request, 'sushisake/index.html')


class GetMenu(View):

    def get(self, request):
        sharers = FoodItem.objects.filter(category='SHARERS')
        platters = FoodItem.objects.filter(category='PLATTERS')
        sushi = FoodItem.objects.filter(category='SUSHI')
        largeplates = FoodItem.objects.filter(category='LARGE PLATES')
        desserts = FoodItem.objects.filter(category='DESSERTS')

        context = {
            'sharers': sharers,
            'platters': platters,
            'sushi': sushi,
            'largeplates': largeplates,
            'desserts': desserts
        }

        return render(request, 'sushisake/menu.html', context)


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'sushisake/contact.html'

    def post(self, request):
        """ """
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Your message has been successfully sent!')
        return redirect('/')


class UserBookings(View):
    def get(self, request):
        bookings = Booking.objects.filter(guest=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'sushisake/user_bookings.html', context)


class EditBooking(View):
    def get(self, request, booking_id):
        queryset = Booking.objects.filter(guest=request.user)
        booking = get_object_or_404(queryset, id=booking_id)

        return render(
            request,
            "sushisake/edit_booking.html",
            {
                'form': AvailabilityForm()
                },
                )

    def post(self, request, booking_id):

        queryset = Booking.objects.filter(guest=request.user)
        booking = get_object_or_404(queryset, id=booking_id)

        form = AvailabilityForm(data=request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been updated')
            return redirect('mybookings')
        else:
            form = AvailabilityForm(instance=booking)

        return render(
            request,
            "sushisake/edit_booking.html",
            {
                'form': form
            },
        )
