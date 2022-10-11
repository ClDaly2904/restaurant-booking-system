""" File contains all the views for sushisake and restaurant bookings """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View
from django.contrib import messages
from restaurantbookings.booking_functions.availability import (
    check_availability)
from .models import Table, Booking, FoodItem, Contact
from .forms import AvailabilityForm, ContactForm


# Create your views here.

class BookingView(FormView):
    """ Renders the availability form where users can make bookings,
    sends user input to check availability function in booking_functions
    to check for available tables. Returns either success or fail flash
    message to user"""
    form_class = AvailabilityForm
    template_name = 'sushisake/availability_form.html'

    def form_valid(self, form):
        """ Checks the form data is valid and creates booking """
        # check that the input data is valid
        data = form.cleaned_data
        tables = Table.objects.all()
        available_tables = []

        # filter the list of tables for the requested location
        location_list = Table.objects.filter(location=data['table_location'])
        # check the availability of tables and that they have enough seats
        check_tables = (check_availability(data['booking_date_time_start'],
                        data['booking_date_time_end'], data['people']))
        # if tables are in the right location and are available,
        # add them to available tables list
        for table in tables:
            if table in location_list and table in check_tables:
                available_tables.append(table)

        # if there is an available table, create Booking object
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
            # Return success message to user
            messages.success(self.request, 'Your booking has been \n'
                             f'successful! Your table has been booked from\n'
                             f' {booking.booking_date_time_start}\n'
                             f' to {booking.booking_date_time_end}')
            return HttpResponseRedirect(reverse('sushisake'))
        else:
            # If no table available, return error message to user
            messages.error(self.request, 'Sorry, the table type for this \n'
                                         'time is full, please try a \n'
                                         'different  time. ')
            return HttpResponseRedirect(reverse('BookTable'))


class GetHomepage(View):
    """ Renders the Sushi & Sake homepage """
    def get(self, request):
        """ Retrieve the index.html template """
        return render(request, 'sushisake/index.html')


class GetMenu(View):
    """ Renders the Sushi & Sake menu. Takes food item objects from
    models and passes to the template """
    def get(self, request):
        """ Get all the Food Item objects and pass them to the template
        in the context """
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
    """ Renders the Contact page including the contact form that
    sends message to the restaurant """
    form_class = ContactForm
    template_name = 'sushisake/contact.html'

    def form_valid(self, form):
        """ Creates a message to the restaurant that can be viewed in the
        backend admin panel or in the admin dashboard if user is authorised """
        # check form data is valid
        data = form.cleaned_data
        # create contact object
        contact = Contact.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            contact_number=data['contact_number'],
            email_address=data['email_address'],
            message=data['message']
        )
        contact.save()
        # return success message to user
        messages.success(self.request, 'Your message has been sent!')
        return HttpResponseRedirect(reverse('contact'))


class UserBookings(View):
    """ Renders the user bookings view. If a guest logs in they can see
    a list of all their bookings """
    def get(self, request):
        """ Retrieves a list of all bookings for the user logged in """
        # filter bookings by the user making the request
        bookings = Booking.objects.filter(guest=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'sushisake/user_bookings.html', context)


class EditBooking(View):
    """ View to allow users to update a booking """
    def get(self, request, booking_id):
        """ Get the requested booking """
        # filter bookings by booking id
        queryset = Booking.objects.filter(id=booking_id)
        booking = get_object_or_404(queryset)
        # return availability form with existing information so that
        # booking can be updated
        return render(
            request,
            "sushisake/edit_booking.html",
            {
                'form': AvailabilityForm(instance=booking)
                },
                )

    def post(self, request, booking_id):
        """ Update requested booking """
        queryset = Booking.objects.filter(id=booking_id)
        booking = get_object_or_404(queryset)

        form = AvailabilityForm(data=request.POST, instance=booking)
        # if form input is valid, update booking with new information
        if form.is_valid():
            form.save()
            # return success message to user
            messages.success(request, 'Your booking has been updated')
            # redirect user back to their previous page
            if request.user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('mybookings')
        else:
            # if form is not valid, don't update the booking
            form = AvailabilityForm(instance=booking)

        return render(
            request,
            "sushisake/edit_booking.html",
            {
                'form': form
            },
        )


class ConfirmDelete(View):
    """ Creates view where users can delete booking objects """
    def get(self, request, booking_id):
        """ Get requested booking """
        queryset = Booking.objects.filter(id=booking_id)
        booking = get_object_or_404(queryset)
        context = {
            'booking_id': booking_id,
            'booking': booking
        }

        return render(
            request,
            "sushisake/confirm_delete.html", context)

    def post(self, request, booking_id):
        """ On confirmation, delete selected booking """
        booking = get_object_or_404(Booking, id=booking_id)

        if request.method == "POST":
            # delete booking
            booking.delete()
            # return success message to user
            messages.success(request, 'Your booking has been cancelled!')
            # redirect user back to their previous page
            if request.user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('mybookings')

        return render(
            request,
            "sushisake/confirm_delete.html")


class AdminDashboard(View):
    """ Creates view for admin dashboard where restaurant staff
    can view a list of all bookings and messages to the restaurant """
    def get(self, request):
        """ Retrieve all booking and message objects """
        bookings = Booking.objects.all()
        contacts = Contact.objects.all()
        context = {
            'bookings': bookings,
            'contacts': contacts
        }
        return render(request, 'sushisake/admin_dashboard.html', context)


class ConfirmClearMessage(View):
    """ Creates view where users can delete booking objects """
    def get(self, request, contact_id):
        """ Get requested message """
        queryset = Contact.objects.filter(id=contact_id)
        contact = get_object_or_404(queryset)
        context = {
            'contact_id': contact_id,
            'contact': contact
        }

        return render(
            request,
            "sushisake/confirm_clear_message.html", context)

    def post(self, request, contact_id):
        """ On confirmation, delete selected message """
        contact = get_object_or_404(Contact, id=contact_id)

        if request.method == "POST":
            # delete message
            contact.delete()
            # return success message to user
            messages.success(request, 'The message has been cleared!')
            # redirect user back to their previous page
            return redirect('admin_dashboard')

        return render(
            request,
            "sushisake/confirm_clear_message.html")
