from django import forms
from django.forms import ModelForm
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

    booking_date_time_start = forms.DateTimeField(
        required=True,
        input_formats=['%d/%m/%YT%H:%M', ],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    booking_date_time_end = forms.DateTimeField(
        required=True,
        input_formats=['%d/%m/%YT%H:%M', ],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

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
