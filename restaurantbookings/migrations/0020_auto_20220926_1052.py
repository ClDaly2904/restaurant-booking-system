# Generated by Django 3.2.15 on 2022-09-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantbookings', '0019_auto_20220922_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='additional_info',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='people',
            field=models.PositiveIntegerField(),
        ),
    ]
