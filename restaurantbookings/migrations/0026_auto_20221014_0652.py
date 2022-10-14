# Generated by Django 3.2.15 on 2022-10-14 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantbookings', '0025_alter_booking_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='first_name',
            field=models.CharField(default='clark', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='last_name',
            field=models.CharField(default='kent', max_length=30),
            preserve_default=False,
        ),
    ]