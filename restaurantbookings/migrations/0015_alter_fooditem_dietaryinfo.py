# Generated by Django 3.2.15 on 2022-09-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantbookings', '0014_alter_fooditem_dietaryinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='dietaryinfo',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
