from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView, View
from django.contrib import messages
from restaurantbookings.booking_functions.availability import check_availability
from .models import Table, Booking, FoodItem, Contact
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
        tables = Table.objects.all()
        available_tables = []

        location_list = Table.objects.filter(location=data['table_location'])
        check_tables = check_availability(data['booking_date_time_start'], data['booking_date_time_end'], data['people'])
        for table in tables:
            if table in location_list and table in check_tables:
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
            return HttpResponseRedirect(reverse('BookTable'))


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

    def form_valid(self, form):
        """ """
        data = form.cleaned_data
        contact = Contact.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            contact_number=data['contact_number'],
            email_address=data['email_address'],
            message=data['message']
        )
        contact.save()
        messages.success(self.request, 'Your message has been sent!')
        return HttpResponseRedirect(reverse('contact'))


class UserBookings(View):
    def get(self, request):
        bookings = Booking.objects.filter(guest=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'sushisake/user_bookings.html', context)


class EditBooking(View):
    def get(self, request, booking_id):
        queryset = Booking.objects.filter(id=booking_id)
        booking = get_object_or_404(queryset)

        return render(
            request,
            "sushisake/edit_booking.html",
            {
                'form': AvailabilityForm(instance=booking)
                },
                )

    def post(self, request, booking_id):

        queryset = Booking.objects.filter(id=booking_id)
        booking = get_object_or_404(queryset)

        form = AvailabilityForm(data=request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been updated')
            if request.user.is_superuser:
                return redirect('admin_dashboard')
            else:
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


class ConfirmDelete(View):
    def get(self, request, booking_id):
        queryset = Booking.objects.filter(id=booking_id)
        booking = get_object_or_404(queryset)

        return render(
            request,
            "sushisake/confirm_delete.html")

    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)

        if request.method == "POST":
            booking.delete()
            messages.success(request, 'Your booking has been cancelled!')
            if request.user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('mybookings')

        return render(
            request,
            "sushisake/confirm_delete.html")


class AdminDashboard(View):
    def get(self, request):
        bookings = Booking.objects.all()
        contactmessages = Contact.objects.all()
        context = {
            'bookings': bookings,
            'contactmessages': contactmessages
        }
        return render(request, 'sushisake/admin_dashboard.html', context)
