# Generated by Django 3.2.15 on 2022-08-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantbookings', '0003_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_end',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(),
        ),
    ]
