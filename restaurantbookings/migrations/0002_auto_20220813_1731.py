# Generated by Django 3.2.15 on 2022-08-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantbookings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='id',
        ),
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
