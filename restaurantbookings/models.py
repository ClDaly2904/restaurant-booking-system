from django.db import models

# Create your models here.


class Table(models.Model):
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
