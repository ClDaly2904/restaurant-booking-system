""" Contains information for the models for the restaurant booking system """
from django.db import models
from django.conf import settings


# Create your models here.
class Table(models.Model):
    """ Contains info on tables, used as foreign key in booking model"""
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
    """ Contains model for booking """
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    people = models.PositiveIntegerField()
    booking_date_time_start = models.DateTimeField()
    booking_date_time_end = models.DateTimeField()
    guest = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    additional_info = models.CharField(max_length=200, blank=True)

    class Meta:
        """ Order by booking start time """
        ordering = ['booking_date_time_start']

    def __str__(self):
        return (f'{self.guest} has booked a table for {self.people}\n'
                f' people for {self.booking_date_time_start} until \n'
                f'{self.booking_date_time_end}')


class FoodItem(models.Model):
    """ Contains information for food items on menu
    including name, price, dietary requirements """
    categories = (
        ('SHARERS', 'sharers'),
        ('PLATTERS', 'platters'),
        ('SUSHI', 'sushi'),
        ('LARGE PLATES', 'large plates'),
        ('DESSERTS', 'desserts'),
    )

    category = models.CharField(max_length=12, choices=categories)
    name = models.CharField(max_length=20)
    dietaryinfo = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name}: {self.price}, {self.dietaryinfo}'


class Contact(models.Model):
    """ Contains information for the contact model so guests can
    send a message to the restaurant """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    contact_number = models.BigIntegerField()
    email_address = models.EmailField(max_length=30)
    message = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ show oldest messages at the top """
        ordering = ["-created_on"]

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.created_on}'
