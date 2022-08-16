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
    min_people = models.IntegerField()
    max_people = models.IntegerField()
    location = models.CharField(max_length=3, choices=TABLE_LOCATION)

    def __str__(self):
        return f'{self.number}: {self.location} min guests {self.min_people}, max guests {self.max_people}'


class Booking(models.Model):
    """Contains info about appointment"""

    class Meta:
        unique_together = ('table', 'date', 'timeslot')

    TIMESLOT_LIST = (
        (0, '09:00 - 10:30'),
        (1, '10:30 - 12:00'),
        (2, '12:00 - 13:30'),
        (3, '13:30 - 15:00'),
        (4, '15:00 - 16:30'),
        (5, '16:30 - 18:00'),
        (6, '18:00 - 19:30'),
        (7, '19:30 - 21:00'),
        (8, '21:00 - 22:30'),
    )

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField(help_text="DD-MM-YY", default=None)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST, default=None)
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guest} has booked {self.table} for {self.timeslot}'

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]
