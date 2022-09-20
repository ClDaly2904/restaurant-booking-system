from django import forms


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


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    contact_number = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
