from django import forms
from django.forms import ModelForm
from .models import Contact


class AvailabilityForm(forms.Form):
    TABLE_LOCATION = (
        ('IN', 'INSIDE SEATING'),
        ('OUT', 'OUTSIDE SEATING')
    )
    table_location = forms.ChoiceField(choices=TABLE_LOCATION, required=True)
    people = forms.IntegerField(required=True)
    booking_date_time_start = forms.DateTimeField(required=True,
                                                  input_formats=['%d/%m/%YT%H:%M', ],
                                                  widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    booking_date_time_end = forms.DateTimeField(required=True,
                                                input_formats=['%d/%m/%YT%H:%M', ],
                                                widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))


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
        # Tell the form to use all the fields provided
        fields = ('first_name', 'last_name', 'email_address', 'contact_number', 'message')

        class Meta:
            fields = '__all__'
