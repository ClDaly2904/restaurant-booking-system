from django import forms


class AvailabilityForm(forms.Form):
    TABLE_LOCATION = (
        ('IN', 'INSIDE SEATING'),
        ('OUT', 'OUTSIDE SEATING')
    )
    table_location = forms.ChoiceField(choices=TABLE_LOCATION, required=True)
    people = forms.IntegerField(required=True)
    booking_date_time_start = forms.DateTimeField(required=True, input_formats=['%m/%d/%Y %H:%M', ])
    booking_date_time_end = forms.DateTimeField(required=True, input_formats=['%m/%d/%Y %H:%M', ])
