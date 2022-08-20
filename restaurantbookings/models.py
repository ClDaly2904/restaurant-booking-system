from django.db import models
from django.conf import settings


# Create your models here.
class Table(models.Model):
    """ Contains info on tables"""
    TABLE_LOCATION = (
        ('IN', 'INSIDE SEATING'),
        ('OUT', 'OUTSIDE SEATING')
    )
    number = models.IntegerField(primary_key=True)
    no_seats = models.IntegerField()
    location = models.CharField(max_length=3, choices=TABLE_LOCATION)

    def __str__(self):
        return f'{self.number}: {self.location}, max people {self.no_seats}'


class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    people = models.IntegerField()
    booking_date_time_start = models.DateTimeField()
    booking_date_time_end = models.DateTimeField()
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guest} has booked a table for {self.people} people for {self.booking_date_time_start} until {self.booking_date_time_end}'