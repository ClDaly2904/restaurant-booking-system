import pytz
from dateutil import parser
from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Contact


class AvailabilityForm(ModelForm):
    TABLE_LOCATION = (
        ('IN', 'INSIDE SEATING'),
        ('OUT', 'OUTSIDE SEATING')
    )

    table_location = forms.ChoiceField(
        choices=TABLE_LOCATION,
        required=True
    )

    people = forms.IntegerField(
        label='Number of people',
        required=True,
        widget=forms.NumberInput({'placeholder': 'Number of people'})
    )

    def clean_people(self):
        data = self.cleaned_data['people']

        # Check only one number input
        if data > 8:
            raise ValidationError(_('Invalid number of people - please enter a number between 1 and 8'))

        # Check user has not entered 0
        if data <= 0:
            raise ValidationError(_('Invalid number of people - please enter a number between 1 and 8'))

        # Return the cleaned data
        return data

    booking_date_time_start = forms.DateTimeField(
        required=True,
        input_formats=['%d/%m/%YT%H:%M', ],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    def clean_booking_date_time_start(self):
        data = self.cleaned_data['booking_date_time_start']
        now = timezone.now()

        # Check if a date is not in the past.
        if data < now:
            raise ValidationError(_('Invalid date/time - please select a date and time in the future.'))

        # check that end time is within opening times
        # get time from datetime obj
        time = data.time()
        # get hour from time
        start_hour = time.hour

        # raise validation error if hour is bigger than or equal to closing
        if start_hour <10:
            raise ValidationError(_('Invalid start time- restaurant opens at 10:00.'))

        # Return the cleaned data.
        return data

    booking_date_time_end = forms.DateTimeField(
        required=True,
        input_formats=['%d/%m/%YT%H:%M', ],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    def clean_booking_date_time_end(self):
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
            raise ValidationError(_('Invalid date/time - please select a date and time in the future.'))

        # check that date time end is after date time start
        if data < start_time:
            raise ValidationError(_('Invalid date/time - please make sure that booking end time is after booking start time.'))

        # check that slot is not longer than 2 hours
        # find differentce between start time and end time
        time_diff = data - start_time
        # find time in seconds
        tsecs = time_diff.total_seconds()
        # multiply to convert time to hours
        thrs = tsecs/(60*60)

        # raise validation error is difference is greater than 2 hours
        if thrs > 2:
            raise ValidationError(_('Invalid end time- maximum slot time is 2 hours.'))

        # check that end time is within opening times
        # get time from datetime obj
        time = data.time()
        # get hour from time
        end_hour = time.hour

        # raise validation error if hour is bigger than or equal to closing
        if end_hour >= 23:
            raise ValidationError(_('Invalid end time- restaurant closes at 23:00.'))

        # Return the cleaned data.
        return data

    additional_info = forms.CharField(
        label='Additional Info',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Please enter any additional information (max 400 characters)', 'rows': 2})
    )

    class Meta:
        """ """
        model = Contact
        fields = ('table_location', 'people', 'booking_date_time_start', 'booking_date_time_end')


class ContactForm(ModelForm):
    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )

    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )

    contact_number = forms.IntegerField(
        label='Contact Number',
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Contact Number'}),
    )

    email_address = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),
    )

    message = forms.CharField(
        label='Message',
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Please enter your message (max 400 characters)', 'rows': 3})
    )

    class Meta:
        """ """
        model = Contact
        fields = ('first_name', 'last_name', 'email_address', 'contact_number', 'message')
