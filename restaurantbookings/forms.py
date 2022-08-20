from django import forms


class AvailabilityForm(forms.Form):
    TABLE_LOCATION = (
        ('IN', 'INSIDE SEATING'),
        ('OUT', 'OUTSIDE SEATING')
    )
    table_location = forms.ChoiceField(choices=TABLE_LOCATION, required=True)
    booking_date_time_start = forms.DateTimeField(required=True, input_formats=["%D-%M-%YT%H-%M"])
    booking_date_time_end = forms.DateTimeField(required=True, input_formats=["%D-%M-%YT%H-%M"])
