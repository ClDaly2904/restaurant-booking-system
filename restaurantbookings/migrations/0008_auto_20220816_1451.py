# Generated by Django 3.2.15 on 2022-08-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantbookings', '0007_auto_20220816_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date_time_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date_time_start',
            field=models.DateTimeField(null=True),
        ),
    ]
