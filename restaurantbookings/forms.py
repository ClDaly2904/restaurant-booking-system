""" File contains all of the inputs and validations for the
availability and contact forms """
import pytz
from dateutil import parser
from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Contact, Booking


class AvailabilityForm(ModelForm):
    """ Sets the inputs for the Availability form """
    TABLE_LOCATION = (
        ('IN', 'INSIDE SEATING'),
        ('OUT', 'OUTSIDE SEATING')
    )

    table_location = forms.ChoiceField(
        choices=TABLE_LOCATION,
        required=True
    )

    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )

    def clean_first_name(self):
        """ Contains validation requirements for the first name input """
        data = self.cleaned_data['first_name']

        if not data.isalpha():
            raise ValidationError(_('Please only enter letters'))

        return data

    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )

    def clean_last_name(self):
        """ Contains validation requirements for last name input """
        data = self.cleaned_data['last_name']

        if not data.isalpha():
            raise ValidationError(_('Please only enter letters'))

        return data

    people = forms.IntegerField(
        label='Number of people',
        required=True,
        widget=forms.NumberInput({'placeholder': 'Number of people'})
    )

    def clean_people(self):
        """ Contains validation for the people input """
        data = self.cleaned_data['people']

        # Check only one number input
        if data > 8:
            raise ValidationError(_('Invalid number of people /n'
                                    '- please enter a number between 1 and 8'))

        # Check user has not entered 0
        if data <= 0:
            raise ValidationError(_('Invalid number of people /n'
                                    '- please enter a number between 1 and 8'))

        # Return the cleaned data
        return data

    booking_date_time_start = forms.DateTimeField(
        required=True,
        input_formats=['%d/%m/%YT%H:%M', ],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    def clean_booking_date_time_start(self):
        """ Contains the validation requirements for the booking start time """
        data = self.cleaned_data['booking_date_time_start']
        now = timezone.now()

        # Check if a date is not in the past.
        if data < now:
            raise ValidationError(_('Invalid date/time - please \n'
                                    'select a date and time in the future.'))

        # check that end time is within opening times
        # get time from datetime obj
        time = data.time()
        # get hour from time
        start_hour = time.hour

        # raise validation error if hour is bigger than or equal to closing
        if start_hour < 10:
            raise ValidationError(_('Invalid start time- restaurant \n'
                                    'opens at 10:00.'))

        # Return the cleaned data.
        return data

    booking_date_time_end = forms.DateTimeField(
        required=True,
        input_formats=['%d/%m/%YT%H:%M', ],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    def clean_booking_date_time_end(self):
        """ Contains the validation requirements for the booking end time """
        data = self.cleaned_data['booking_date_time_end']
        now = timezone.now()
        start_time_input = self.data['booking_date_time_start']
        # convert to datetime obj
        start_time_ntz = parser.parse(start_time_input)
        # add timezone
        t_z = pytz.timezone("UTC")
        start_time = t_z.localize(start_time_ntz)

        # Check if a date is not in the past.
        if data < now:
            raise ValidationError(_('Invalid date/time - please select a \n'
                                    'date and time in the future.'))

        # check that date time end is after date time start
        if data < start_time:
            raise ValidationError(_('Invalid date/time - please make sure \n'
                                    'that booking end time is after \n'
                                    'booking start time.'))

        # check that slot is not longer than 2 hours
        # find differentce between start time and end time
        time_diff = data - start_time
        # find time in seconds
        tsecs = time_diff.total_seconds()
        # multiply to convert time to hours
        thrs = tsecs/(60*60)

        # raise validation error is difference is greater than 2 hours
        if thrs > 2:
            raise ValidationError(_('Invalid end time- maximum slot \n'
                                    'time is 2 hours.'))

        # check that end time is within opening times
        # get time from datetime obj
        time = data.time()
        # get hour from time
        end_hour = time.hour

        # raise validation error if hour is bigger than or equal to closing
        if end_hour >= 23:
            raise ValidationError(_('Invalid end time- restaurant closes \n'
                                    'at 23:00.'))

        # Return the cleaned data.
        return data

    additional_info = forms.CharField(
        label='Additional Info',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Please enter \n'
                                     'any additional information (max \n'
                                     '400 characters)', 'rows': 2})
    )

    class Meta:
        """ Specifies to use the booking model """
        model = Booking
        fields = ('first_name', 'last_name', 'table_location',
                  'people', 'booking_date_time_start',
                  'booking_date_time_end', 'additional_info')


class ContactForm(ModelForm):
    """ Contains for the information for the contact form """
    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )

    def clean_first_name(self):
        """ Contains validation requirements for the first name input """
        data = self.cleaned_data['first_name']

        if not data.isalpha():
            raise ValidationError(_('Please only enter letters'))

        return data

    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )

    def clean_last_name(self):
        """ Contains validation requirements for last name input """
        data = self.cleaned_data['last_name']

        if not data.isalpha():
            raise ValidationError(_('Please only enter letters'))

        return data

    contact_number = forms.IntegerField(
        label='Contact Number',
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Contact Number'}),
    )

    def clean_contact_number(self):
        """ Contains validation requirements for the contact number input """
        data = self.cleaned_data['contact_number']

        # convert data to string and check length is phone number
        if not 11 >= len(str(data)) >= 12:
            raise ValidationError(_('Please enter a valid phone number'))

        return data

    email_address = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),
    )

    message = forms.CharField(
        label='Message',
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Please enter your \n'
                                     'message (max 400 characters)',
                                     'rows': 3})
    )

    def clean_message(self):
        """ Contains validation information for the message input """
        data = self.cleaned_data['message']

        # check to see that message isn't just spaces
        if data.isspace():
            raise ValidationError(_('Please enter a message'))

        if len(data) < 10:
            raise ValidationError(_('Minimum value 10 characters'))

        return data

    class Meta:
        """ Specifies to use contact model as a base """
        model = Contact
        fields = ('first_name', 'last_name', 'email_address',
                  'contact_number', 'message')
