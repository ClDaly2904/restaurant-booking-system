from django.contrib import admin
from .models import Table, Booking, FoodItem


# Register your models here.
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(FoodItem)
