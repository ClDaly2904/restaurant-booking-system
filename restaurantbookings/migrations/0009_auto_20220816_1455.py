# Generated by Django 3.2.15 on 2022-08-16 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantbookings', '0008_auto_20220816_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date_time_end',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_date_time_start',
        ),
    ]
